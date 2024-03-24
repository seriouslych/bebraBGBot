import asyncio
from aiogram.types import Message
from log import log


async def pid_message(message: Message):
    await message.reply(f"Отправь мне <b>в ответ</b> изображение чтобы узнать её ID!", parse_mode='HTML')
    
async def pid_handler(message: Message):
    if message.reply_to_message:
        try:
            await pid_get(message)
        except Exception as e:
            log.exception(e)

async def pid_get(message: Message):
    photo = message.photo[-1]
    await message.reply(f"ID фото: <code>{photo.file_id}</code>", parse_mode='HTML')    
    
async def bebra_message(message: Message):
    await message.reply_photo(photo='AgACAgIAAxkBAAPMZgABJpre-9PZ17lwwAiukPREkCeiAAKT4DEbS6MBSD2ayU5F5mS1AQADAgADeQADNAQ', caption='bebra')
