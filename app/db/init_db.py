import asyncio
from app.db.session import engine
from app.models.base import Base
import app.models

async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
	asyncio.run(init_db())
