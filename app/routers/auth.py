from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserRegisterRequest, UserRegisterResponse
from app.services.auth_service import create_user, create_auth_tokens
from app.services.token_service import TokenService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRegisterResponse)
async def register_user(user_data: UserRegisterRequest, session: Session = Depends(get_db)):
	user = await create_user(user_data, session)

	payload = {"sub": str(user.id), "email": user.email}
	access_token, refresh_token = await TokenService.create_auth_tokens(user, payload, session)
	
	response = UserRegisterResponse(access_token, refresh_token)
	return response
