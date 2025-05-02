from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserRegisterRequest, UserRegisterResponse
from app.services.auth_service import create_user
from app.services.token_service import TokenService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRegisterResponse)
async def register_user(user_data: UserRegisterRequest, session: AsyncSession = Depends(get_db)):
	user_info = await create_user(user_data, session)

	payload = {"sub": str(user_info.id)}
	access_token, refresh_token = await TokenService.create_auth_tokens(user_info, payload, session)
	
	response = UserRegisterResponse(access_token=access_token,
									refresh_token=refresh_token,
									user=user_info)
	return response
