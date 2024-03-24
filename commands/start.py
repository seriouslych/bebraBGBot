import asyncio
from aiogram.types import Message


async def start_message(message: Message):
    await message.reply("""
                 Бот который умеет делать всякие вещи.\n\n<b>Команды бота:</b>
    /start и /help - помощь
    /bebra - бебрить
    /vid [ссылка] - скачивать видео с ютуба
    /aud [ссылка] - скачивать аудио с ютуба
    /stk - преобразование изображения в размер подходящий для стикера
                 """,
                        parse_mode='html')
