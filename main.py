from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.user import router as user_router

app = FastAPI(
	title="Booking Service API",
	version="1.0.0",
	description="This API allows users to book slots, create events, and manage their availability.",
	contact={
		"name": "Agvan Grigoryan",
		"email": "agvangrigoryan2003@gmail.com",
	},
	license_info={
		"name": "MIT License",
		"url": "https://opensource.org/licenses/MIT",
	},
	)

app.include_router(auth_router)
app.include_router(user_router)