import os
import time

from PIL import Image

def sticker_message(bot, message, cancel_inline):
    bot.reply_to(message, "🏞 Отправь мне изображение в ответ, чтобы обработать её как стикер", reply_markup=cancel_inline)
    
def photo_stk_get(bot, message, base_dir):
    get = bot.reply_to(message, "🛜 Получение изображения...")
    
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        photo_download = bot.download_file(file_info.file_path)
        
        temp_dir = os.path.join(base_dir, 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        input_path = os.path.join(temp_dir, 'photo.jpg')
        output_path = os.path.join(temp_dir, 'sticker.png')
        
        with open(input_path, 'wb') as photo:
            photo.write(photo_download)
        
        time.sleep(1.5)
        got = bot.edit_message_text("✅ Изображение получено", message.chat.id, get.message_id)
        time.sleep(1)
        process = bot.edit_message_text("🔄 Обработка изображения...", message.chat.id, got.message_id)
        
        photo_process(bot, message, input_path, output_path, process)
        
    except Exception as e:
        bot.edit_message_text(message.chat.id, get.message_id, "❌ Ошибка получения изображения!")
        print(e)
    
def photo_stk_except(bot, message):
    bot.reply_to(message, "Отправь мне изображение в ответ, балбес")
    
def photo_process(bot, message, input_path, output_path, process):
    try:
        # Открываем изображение
        image = Image.open(input_path)

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
        cropped_image.save(output_path, "PNG")
        
        photo_stk_send(bot, message, input_path, output_path, process)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
def photo_stk_send(bot, message, input_path, output_path, process):
    bot.edit_message_text("✅ Готово!", message.chat.id, process.message_id)
    with open(output_path, 'rb') as doc:
        bot.send_document(message.chat.id, doc)

    os.remove(input_path)
    os.remove(output_path)
