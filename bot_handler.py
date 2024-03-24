import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from log import log

from commands.bebra import *
from commands.start import *

token = '6464094470:AAF57DSStRaFNz6O8mlSGzntsK864wgGvUI'
log.info("Инициализация...")

try:
    bot = Bot(token)
    dp = Dispatcher()
    log.info("Инициализировано!")

    async def main():
        await dp.start_polling(bot)

except Exception as e:
    log.exception(e)


@dp.message(Command('start', 'help'))
async def start(message: Message):
    await start_message(message)
    log.info(f"[@{message.from_user.username}] Отправлена помощь.")

@dp.message(Command('pid'))
async def pid(message: Message):
    await pid_message(message)

@dp.message(F.photo)
async def pid_start(message: Message):
    await pid_handler(message)
    
@dp.message(Command('bebra'))
async def bebra(message: Message):
    await bebra_message(message)


if __name__ == '__main__':
    asyncio.run(main())
