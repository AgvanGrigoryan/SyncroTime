from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL


engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
	engine,
	class_=AsyncSession,
	autoflush=False,
	expire_on_commit=False
)

async def get_db():
	async with SessionLocal() as session:
		yield session