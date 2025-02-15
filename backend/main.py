from fastapi import FastAPI

from backend.routers.user import user_router

app = FastAPI()

app.include_router(user_router)
