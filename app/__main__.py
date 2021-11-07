import uvicorn

from app.db import metadata, engine
from app.db.images import images

from app.base import init_app


app = init_app()

if __name__ == "__main__":
    metadata.create_all(engine)
    uvicorn.run(app, host='127.0.0.1', port=8000)
