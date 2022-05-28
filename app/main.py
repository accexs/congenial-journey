from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()


@app.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong!',
        'environment': settings.environment,
        'testing': settings.testing
    }


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
