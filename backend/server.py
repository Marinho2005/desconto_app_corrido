import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import settings
from src.middlewares.error_handler import RequestLoggingMiddleware
from src.routes.discount_routes import router as discount_router

def create_app() -> FastAPI:
    """Application factory for FastAPI backend."""
    app = FastAPI(
        title="Desconto App API",
        version="1.0.0",
        description="Backend API para cálculo e gerenciamento de descontos"
    )

    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggingMiddleware)

    # Healthcheck Route
    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "ok", "environment": settings.ENVIRONMENT}

    # Register API Routes
    app.include_router(discount_router, prefix="/api")

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=(settings.ENVIRONMENT == "development")
    )

