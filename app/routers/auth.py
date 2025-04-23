from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserRegisterRequest
from app.services.auth_service import create_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register_user(user_data: UserRegisterRequest, session: Session = Depends(get_db)):
	user = create_user(user_data, session)

