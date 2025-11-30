"""Authentication API routes."""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, User
from auth.schemas import (
    UserRegisterRequest,
    UserRegisterResponse,
    UserLoginRequest,
    TokenResponse,
    TokenRefreshRequest,
    UserResponse,
    MessageResponse,
)
from auth.service import register_user, authenticate_user, create_tokens, refresh_tokens
from auth.dependencies import get_current_user


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserRegisterResponse)
async def register(
    data: UserRegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Register a new user.
    
    - **email**: Valid email address (unique)
    - **password**: Minimum 8 characters
    - **name**: User's display name
    """
    user = await register_user(db, data)
    return UserRegisterResponse(
        user_id=user.id,
        message="User registered successfully"
    )


@router.post("/login", response_model=TokenResponse)
async def login(
    data: UserLoginRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Login and get access tokens.
    
    Returns access_token and refresh_token.
    """
    user = await authenticate_user(db, data.email, data.password)
    tokens = create_tokens(user)
    return TokenResponse(**tokens)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(
    data: TokenRefreshRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Refresh access token using refresh token.
    
    Use this when access_token expires.
    """
    tokens = await refresh_tokens(db, data.refresh_token)
    return TokenResponse(**tokens)


@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: User = Depends(get_current_user),
):
    """
    Get current user information.
    
    Requires valid access_token in Authorization header.
    """
    return UserResponse.model_validate(current_user)


@router.post("/logout", response_model=MessageResponse)
async def logout(
    current_user: User = Depends(get_current_user),
):
    """
    Logout current user.
    
    Note: With JWT, logout is handled client-side by removing tokens.
    This endpoint is for consistency and future token blacklist implementation.
    """
    # In a production system, you might want to:
    # 1. Add refresh_token to a blacklist
    # 2. Invalidate all sessions
    # For now, just return success (client removes tokens)
    return MessageResponse(message="Successfully logged out")
