import databases
from fastapi import FastAPI
from config import get_config
import app.views.images as avt

config = get_config()
db_url = f'postgresql://{config.db.username}:{config.db.password}@{config.db.host}:{config.db.port}/{config.db.name}'

database = databases.Database(db_url)


def init_app():
    app = FastAPI()
    app.include_router(router=avt.api_router)

    app.add_event_handler('startup', db_startup)
    app.add_event_handler('shutdown', db_shutdown)
    return app


async def db_startup():
    await database.connect()


async def db_shutdown():
    await database.disconnect()
