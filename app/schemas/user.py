from pydantic import BaseModel, EmailStr, SecretStr,ConfigDict, field_validator
from typing import Optional
import string
from app.schemas.token import JWTTokensResponse

class UserBase(BaseModel):
	name: str
	surname: str
	email: EmailStr
	description: Optional[str] = None	

class UserInfo(UserBase):
	id: int

	model_config = ConfigDict(from_attributes=True)

class UserRegisterRequest(UserBase):
	model_config = ConfigDict(extra="forbid")

	password: SecretStr

	@field_validator("password", mode="after")
	def validate_password(cls, password: SecretStr) -> SecretStr:
		actual_pass = password.get_secret_value()
		if len(actual_pass) < 8:
			raise ValueError("Password must be longer than 8 symbols")
		has_digit = any(char.isdigit() for char in actual_pass)
		has_upper = any(char.isupper() for char in actual_pass)
		has_symbol = any(char in string.punctuation for char in actual_pass)
		if not (has_digit and has_upper and has_symbol):
			raise ValueError("Password must include at least one digit, one uppercase letter and one special symbol")
		return password
	
class UserRegisterResponse(JWTTokensResponse):
	user: UserInfo
