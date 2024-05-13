from aiogram import Bot, Dispatcher, html

from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
WEBHOOK_PATH = os.getenv("TELEGRAM_TOKEN")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
