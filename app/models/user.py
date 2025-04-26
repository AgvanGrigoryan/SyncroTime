from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship
from app.models.base import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True, nullable=False)
	name = Column(String(50), index=True, nullable=False)
	surname = Column(String(50), index=True, nullable=False)
	email = Column(String(100), unique=True, index=True, nullable=False)
	password_hash = Column(String(255), nullable=False)
	description = Column(String(500), nullable=True)
	is_active = Column(Boolean, default=True)
	
	refresh_token = relationship("RefreshToken", back_populates="user")
	# is_verified = Column() to email verification
	# relationship to connect with slots models
