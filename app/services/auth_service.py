from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy import select
from app.schemas.user import UserRegisterRequest, UserInfo
from app.models.user import User
from app.core.security import hash_password, verify_password

async def create_user(user_data: UserRegisterRequest, db: AsyncSession) -> UserInfo:
	user_dict = user_data.model_dump(exclude_unset=True, exclude=["password"])
	password_hash = hash_password(user_data.password.get_secret_value())
		
	existing_user = await db.execute(select(User).filter_by(email=user_data.email))
	existing_user = existing_user.scalars().first()

	if existing_user:
		raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Email '{user_data.email}' is already registered.",
        )

	user = User(**user_dict, password_hash=password_hash)

	db.add(user)
	await db.flush()
	await db.refresh(user)
	await db.commit()
	return UserInfo.model_validate(user)
