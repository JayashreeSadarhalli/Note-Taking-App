import os


class Settings:
    PORT = os.getenv("PORT", 5000)
    DEBUG_MODE = bool(os.getenv("DEBUG_MODE", False))
    MONGODB_URL = os.getenv(
        "MONGODB_URL",
        "mongodb+srv://m001-student:LNQz0uz5xLXRKlJj@sandbox.ue4rv.mongodb.net/?retryWrites=true&w=majority",
    )
    REDIS_URL = os.getenv(
        "REDIS_URL",
        "",
    )
    VERSION = "0.0.0"


settings = Settings()
