"""Pydantic schemas for authentication."""
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


# ============ Request Schemas ============

class UserRegisterRequest(BaseModel):
    """Request schema for user registration."""
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)
    name: str = Field(..., min_length=1, max_length=100)


class UserLoginRequest(BaseModel):
    """Request schema for user login."""
    email: EmailStr
    password: str


class TokenRefreshRequest(BaseModel):
    """Request schema for token refresh."""
    refresh_token: str


# ============ Response Schemas ============

class UserResponse(BaseModel):
    """Response schema for user data."""
    id: int
    email: str
    name: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Response schema for authentication tokens."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds


class MessageResponse(BaseModel):
    """Generic message response."""
    message: str


class UserRegisterResponse(BaseModel):
    """Response schema for user registration."""
    user_id: int
    message: str
