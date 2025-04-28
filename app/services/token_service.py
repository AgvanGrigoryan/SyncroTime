from typing import Literal
import base64
import json
import hmac
import hashlib
from time import time

from sqlalchemy.orm import Session

from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.core.config import JWT_SECRET


class TokenService:
	token_expires_time = {
		"access": 3600,
		"refresh": 3600 * 24
	}

	@staticmethod
	async def save_refresh_token(refresh_token: str, user_id: int, created_at: int, expires_at: int, db: Session):
		refresh = RefreshToken(
			user_id=user_id,
			token_hash = refresh_token,
			created_at = created_at,
			expires_at = expires_at
		)
		db.add(refresh)
		await db.commit()
		await db.refresh(refresh)

	@classmethod
	async def create_auth_tokens(cls, user: User, payload: dict, db: Session):
		now = int(time())

		access_token, _ = cls.create_jwt(payload, "access", now)
		refresh_token, expires_at = cls.create_jwt(payload, "refresh", now)
		cls.save_refresh_token(refresh_token, user.id, now, expires_at, db)

		return access_token, refresh_token

	@staticmethod
	def base64url_encode(data: bytes) -> str:
		return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")

	@classmethod
	def create_jwt(cls, payload: dict, type: Literal["access", "refresh"], now: int):
		expires_at = cls.token_expires_time[type]
		header = {"alg": "HS256", "typ": "JWT"}
		full_payload = {
			**payload,
			"exp": expires_at,
			"type": type,
			"iat": now
		}
		header_b64 = cls.base64url_encode(json.dumps(header, separators=(",", ":")).encode())
		payload_b64 = cls.base64url_encode(json.dumps(full_payload, separators=(",", ":")).encode())
		signature_input = f"{header_b64}.{payload_b64}".encode()
		signature = hmac.new(JWT_SECRET.encode(), signature_input, hashlib.sha256).digest()
		signature_b64 = cls.base64url_encode(signature)
		token = f"{header_b64}.{payload_b64}.{signature_b64}"
		return token, expires_at