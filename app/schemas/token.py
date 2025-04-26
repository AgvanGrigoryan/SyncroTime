from pydantic import BaseModel

class BaseTokensResponse(BaseModel):
	access_token: str
	refresh_token: str
	token_type: str

class JWTTokensResponse(BaseTokensResponse):
	token_type: str = "bearer"