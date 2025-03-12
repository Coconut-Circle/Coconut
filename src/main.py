from fastapi import FastAPI
from src.api.routers import api_router

app = FastAPI(
    title="Coconut Backend 🥥",
    description="Contact [Dileep](https://coconut-ipk6693.slack.com/team/U08GD6RH2RX) for any queries",
    version="1.0.0"
)
# Include all the API routes in the app
app.include_router(api_router)
