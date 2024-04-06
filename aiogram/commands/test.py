import asyncio
import os

from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
version = os.getenv('version')

async def test_message(message: Message):
    await message.reply(f"""
Тест
                        
<code>bebraBGBot {version}</code>
                        """, parse_mode='HTML')