from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL:str
    JWT_SECRET:str
    JWT_ALGORITHM:str="HS256"
    REDIS_HOST:str="redis"
    REDIS_PORT:int=6379
    class Config:
        env_file=".env"
settings=Settings()
