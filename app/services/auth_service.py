from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.session import get_db
from app.schemas.user import UserRegisterRequest
from app.models.user import User
from app.core.security import hash_password, verify_password

async def create_user(user_data: UserRegisterRequest, db: Session):
	password_hash = hash_password(user_data.password)
	user = User(
		name = user_data.name,
		surname = user_data.surname,
		email = user_data.email,
		password_hash = password_hash
	)
	if "description" in user_data.model_fields_set:
		user.description = user_data.description

	db.add(User)

	db.commit()
	db.refresh(User)
	return user