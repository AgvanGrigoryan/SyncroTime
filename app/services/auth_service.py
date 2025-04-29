from sqlalchemy.orm import Session

from app.schemas.user import UserRegisterRequest, UserInfo
from app.models.user import User
from app.core.security import hash_password, verify_password

async def create_user(user_data: UserRegisterRequest, db: Session) -> UserInfo:
	user_dict = user_data.dict(exclude_unset=True)
	password_hash = hash_password(user_data.password.get_secret_value())
	user = User(**user_dict, password_hash=password_hash)

	db.add(user)
	db.commit()
	db.refresh(user)
	return UserInfo.model_validate(user)
