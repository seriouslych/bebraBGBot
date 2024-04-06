import asyncio
import os

from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
version = os.getenv('version')


async def start_message(message: Message):
    await message.reply(f"""
Бот который умеет делать всякие вещи
    
    <b>Команды бота:</b>
    /start и /help - помощь
    /bebra - бебрить
    /pid - получить ID изображения
    
<code>bebraBGBot {version}</code>
                        """,
                        parse_mode='html')
