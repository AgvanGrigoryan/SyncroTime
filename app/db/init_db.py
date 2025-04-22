from app.db.session import engine
from app.models import user

async def init_db():
	user.DeclarativeBase.metadata.create_all(bind=engine)