
from fastapi import Depends
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from app.core.security import security
from app.services.token_service import TokenService
from app.models.user import User
from app.db.session import get_db

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: AsyncSession = Depends(get_db)) -> User:
    token = credentials.credentials
    payload = TokenService.decode_jwt(token)
    try:
        user_id = int(payload.get("sub", None))
    except (TypeError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token subject")
    
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

