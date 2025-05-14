from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.core.security import security
from app.models.user import User
from app.schemas.user import UserBase
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(security)])

@router.get("/me", response_model=UserBase)
async def get_me(user: User = Depends(get_current_user)):
    return UserBase.model_validate(user)