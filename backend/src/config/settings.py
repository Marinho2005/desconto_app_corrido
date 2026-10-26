import os


class Settings:
    """Configurações carregadas a partir do ambiente."""

    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))


settings = Settings()
