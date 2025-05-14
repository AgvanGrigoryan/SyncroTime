from passlib.context import CryptContext
from fastapi.security import HTTPBearer

context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

def hash_password(password: str) -> str:
	return context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
	return context.verify(plain_password, hashed_password)