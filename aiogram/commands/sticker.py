import asyncio

from PIL import Image
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.log import log 

router = Router()
    
async def sticker_convert(photo_path, sticker_path, message: Message):
    await message.reply("⏩ Конвертирование...")
    
    try:
        # Открываем изображение
        image = Image.open(photo_path)

        # Обрезаем или изменяем размер изображения до 512x512 пикселей
        width, height = image.size
        if width != height or width != 512:
            # Определяем координаты обрезки
            left = 0
            top = 0
            right = width
            bottom = height
            if width > height:
                # Обрезаем по горизонтали
                left = (width - height) // 2
                right = left + height
            elif height > width:
                # Обрезаем по вертикали
                top = (height - width) // 2
                bottom = top + width
            # Обрезаем или изменяем размер
            cropped_image = image.crop((left, top, right, bottom)).resize((512, 512), Image.BICUBIC)
        else:
            # Изменяем размер
            cropped_image = image.resize((512, 512), Image.BICUBIC)

        # Сохраняем обработанное изображение
        cropped_image.save(sticker_path, "PNG")
        
        await sticker_send(message, sticker_path)
        

    except Exception as e:
        log.exception(e)
        
async def sticker_send(message: Message, sticker_path):
    await message.answer_document(document=sticker_path, caption="✅ Готово!")
