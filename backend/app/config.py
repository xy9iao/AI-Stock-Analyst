import os


class Config:
    APP_ENV = os.getenv("APP_ENV", "development")
    DATABASE_URL = os.getenv(
        "DB_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/stock_analytics"
    )
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    STOCK_API_KEY = os.getenv("STOCK_API_KEY", "")
