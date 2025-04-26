import asyncio
from app.db.session import engine
from app.models.base import Base
from app.models.user import User
from app.models.refresh_token import RefreshToken

async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
	asyncio.run(init_db())
