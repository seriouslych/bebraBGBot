import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from log import log
from start import *
from bebra import *

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
    try:
        await pid_message(message)
        log.info(f"[@{message.from_user.username}] Отправлен ID изображения.")
    except Exception as e:
        log.exception(e)


@dp.message(F.photo)
async def pid_get(message: Message):
    replied_message = message.reply_to_message
    if replied_message and replied_message.photo:
        await message.reply(f"ID фото: <code>{message.photo[-1].file_id}</code>", parse_mode='html')


if __name__ == '__main__':
    asyncio.run(main())
