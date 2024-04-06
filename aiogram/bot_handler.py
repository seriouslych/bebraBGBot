import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from aiogram.log import log
from dotenv import load_dotenv

from commands.start import *
from commands.bebra import *
from commands.sticker import *
from commands.test import *
from commands import sticker
from commands import bebra


load_dotenv()

token = os.getenv('token')

reply_sticker = False

log.info("Инициализация...")

try:
    bot = Bot(token)
    dp = Dispatcher()
    log.info("Инициализировано!")
    
    dp.include_routers(
        sticker.router,
        bebra.router
        )
    
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
    wait_photoid = True
    await pid_message(message)
    
@dp.message(Command('stk'))
async def sticker(message: Message):
    wait_sticker = True
    await sticker_message(message)
    
async def sticker_message(message: Message):
    global reply_sticker
    await message.reply("🏞 Отправь мне изображение в ответ, чтобы обработать её как стикер")
    reply_sticker = True
    
@dp.message(F.photo)
async def sticker_handler(message: Message):
    global reply_sticker
    if message.reply_to_message and reply_sticker:
        try:
            await sticker_get(message)
        except Exception as e:
            log.exception(e)
    reply_sticker = False
        
    
async def sticker_get(message: Message):
    photo = message.photo[-1]

    await bot.download(photo, destination='D:/!Projects/Bots/Telegram/bebraBGBot/temp/photo.jpg')
    photo_path = 'D:/!Projects/Bots/Telegram/bebraBGBot/temp/photo.jpg'
    sticker_path = FSInputFile("D:/!Projects/Bots/Telegram/bebraBGBot/temp/sticker.png")
    
    await sticker_convert(photo_path, sticker_path, message)
    
@dp.message(Command('bebra'))
async def bebra(message: Message):
    await bebra_message(message)
    
@dp.message(Command('t'))
async def test(message: Message):
    await test_message(message)

if __name__ == '__main__':
    asyncio.run(main())