import asyncio
import logging
import os
import sys

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from DB.db import collection

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    user_data = {
        '_id': message.from_user.id,
        'username': message.from_user.username,
    }

    if collection.find_one({"_id": user_data["_id"]}):
        await message.answer(f"I am glad to see you again {message.from_user.full_name}!")
    else:
        collection.insert_one(user_data)

        await message.answer(f"Hi {message.from_user.full_name}! I sent information about you to SBU! Good Night!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

