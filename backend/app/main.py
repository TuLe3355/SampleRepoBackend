from fastapi import FastAPI
from app.api import router as api_router


def create_app() -> FastAPI:
    application = FastAPI(
        title="Sample FastAPI Server"
    )

    application.include_router(api_router)
    return application



app = create_app()