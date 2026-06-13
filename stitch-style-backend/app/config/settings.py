from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    JWT_SECRET: str
    JWT_REFRESH_SECRET: str
    FIREBASE_CREDENTIALS_JSON: str
    RAZORPAY_KEY_ID: str
    RAZORPAY_SECRET: str
    CLOUDINARY_URL: str
    PORT: int = 8000
    ENV: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
