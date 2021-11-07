import uvicorn

from app.base import init_app


app = init_app()

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
