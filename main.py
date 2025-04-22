from fastapi import FastAPI

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