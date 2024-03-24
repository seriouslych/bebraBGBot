import asyncio
from aiogram.types import Message


async def pid_message(message: Message):
    await message.reply(f"Отправь мне в **ответ** изображение чтобы узнать её ID!", parse_mode='markdown')
