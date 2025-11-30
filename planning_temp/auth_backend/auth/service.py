"""Authentication business logic."""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from fastapi import HTTPException, status

from database.models import User
from auth.schemas import UserRegisterRequest
from auth.jwt_handler import create_access_token, create_refresh_token, verify_token, get_token_expires_in


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    """Get a user by email."""
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    """Get a user by ID."""
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def register_user(db: AsyncSession, data: UserRegisterRequest) -> User:
    """
    Register a new user.
    
    Raises:
        HTTPException: If email already exists
    """
    # Check if email exists
    existing_user = await get_user_by_email(db, data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create user
    user = User(
        email=data.email,
        hashed_password=hash_password(data.password),
        name=data.name,
    )
    
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    return user


async def authenticate_user(db: AsyncSession, email: str, password: str) -> User:
    """
    Authenticate a user.
    
    Raises:
        HTTPException: If credentials are invalid
    """
    user = await get_user_by_email(db, email)
    
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )
    
    return user


def create_tokens(user: User) -> dict:
    """Create access and refresh tokens for a user."""
    return {
        "access_token": create_access_token(user.id, user.email),
        "refresh_token": create_refresh_token(user.id),
        "token_type": "bearer",
        "expires_in": get_token_expires_in(),
    }


async def refresh_tokens(db: AsyncSession, refresh_token: str) -> dict:
    """
    Refresh access token using refresh token.
    
    Raises:
        HTTPException: If refresh token is invalid or user not found
    """
    # Verify refresh token
    payload = verify_token(refresh_token, token_type="refresh")
    user_id = int(payload["sub"])
    
    # Get user
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )
    
    return create_tokens(user)
