from fastapi import FastAPI
from app.api.feature_router import router as feature_router
from app.api.blacklist_router import router as blacklist_router
from app.config.settings import settings
from app.exceptions.global_exception_handler import global_exception_handler


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="1.0.0",
        description="Feature service for real-time fraud detection (R1–R9)."
    )

    # Routers
    app.include_router(feature_router)
    app.include_router(blacklist_router)

    # Health check
    @app.get("/health")
    async def health():
        return {"status": "UP"}

    # Register global exception handler
    app.add_exception_handler(Exception, global_exception_handler)

    return app


app = create_app()
