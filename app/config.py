from functools import lru_cache
from pydantic import BaseSettings


class Database(BaseSettings):
    host: str = 'localhost'
    port: int = 5432
    username: str = 'postgres'
    password: str = 'postgres'
    name: str = 'postgres'


class Settings(BaseSettings):
    db: Database = Database()


@lru_cache()
def get_config():
    return Settings()
