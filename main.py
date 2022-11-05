import os
import logging

from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy import select
from database.db import session
from database.tables import Questions



token = os.getenv('TELEGRAM_KEY')

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    stmt = select(Questions)
    answer = session.execute(stmt).all()
    # print(answer)
    # executor.start_polling(dp, skip_updates=True)