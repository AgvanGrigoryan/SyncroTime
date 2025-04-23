from app.db.session import engine
from sqlalchemy.orm import DeclarativeBase

async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(DeclarativeBase.metadata.create_all)
