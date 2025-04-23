from sqlalchemy import String, Integer, Column, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime, timezone

class RefreshToken(DeclarativeBase):
	__tablename__ = "refresh_tokens"

	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
	token_hash = Column(String(255), nullable=False)
	created_at = Column(DateTime, default=datetime.now(timezone.utc))
	expires_at = Column(DateTime, nullable=False)

	user = relationship("User", back_populates="refresh_token")