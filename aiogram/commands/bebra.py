import asyncio

from aiogram import F, Router
from aiogram.types import Message
from aiogram.log import log

router = Router()
reply_bebra = False

async def pid_message(message: Message):
    global reply_bebra
    await message.reply(f"Отправь мне <b>в ответ</b> изображение чтобы узнать её ID!", parse_mode='HTML')
    reply_bebra = True
    
@router.message(F.photo)
async def pid_handler(message: Message):   
    global reply_bebra
    if message.reply_to_message and reply_bebra:
        try:
            await pid_get(message)
        except Exception as e:
            log.exception(e)
        reply_bebra = False

async def pid_get(message: Message):
    photo = message.photo[-1]
    await message.reply(f"ID фото: <code>{photo.file_id}</code>", parse_mode='HTML')    
    
async def bebra_message(message: Message):
    await message.reply_photo(photo='AgACAgIAAxkBAAPMZgABJpre-9PZ17lwwAiukPREkCeiAAKT4DEbS6MBSD2ayU5F5mS1AQADAgADeQADNAQ', caption='bebra')
