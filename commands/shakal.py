import os
import time

from PIL import Image

def shakal_message(bot, message, cancel_inline):
    bot.reply_to(message, "🏞 Отправь мне изображение в ответ, чтобы отшакалить его", reply_markup=cancel_inline)
    
def photo_sl_get(bot, message, log, base_dir):
    get = bot.reply_to(message, "🛜 Получение изображения...")
    
    log.info(f"[@{message.from_user.username}] - Обработка изображения...")
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        photo_download = bot.download_file(file_info.file_path)
        
        temp_dir = os.path.join(base_dir, 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        input_path = os.path.join(temp_dir, 'photo.jpg')
        output_path = os.path.join(temp_dir, 'shakal.jpg')
        
        with open(input_path, 'wb') as photo:
            photo.write(photo_download)
            
        time.sleep(1.5)
        got = bot.edit_message_text("✅ Изображение получено", message.chat.id, get.message_id)
        time.sleep(1)
        bot.edit_message_text("🔄 Обработка изображения...", message.chat.id, got.message_id)
    except Exception as e:
        log.exception("Ошибка при получении изображения: ", e)

# Павел дуров иди нахуй пидорас ебаный я твой рот ебал петушаара ебливый 👿
        
def photo_compress(bot, message, input_path, output_path, process, log):
    try:
        # Я ГРАЖДАНСКИЙ Я ГРАЖДАНСКИЙ 🔫🔫🔫💥💥💥
            
        img = Image.open('D:/!Projects/Bots/Telegram/bebraBGBot/temp/photo.jpg')
        
        img.load()
        
        img.save(output_path, quality=10)
        
        photo_sl_send(bot, message, input_path, output_path, process, log)
    except Exception as e:
        log.exception("Ошибка сжатия файла: ", e)
    
def photo_sl_send(bot, message, input_path, output_path, process, log):
    bot.edit_message_text("✅ Готово!", message.chat.id, process.message_id)
    try:
        with open(output_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        log.info(f"[@{message.from_user.username}] - Фото сжато и отправлено.")
    except Exception as e:
        log.exception("Ошибка отправки фото: ", e)
        
    os.remove(input_path)
    os.remove(output_path)

# Павел дуров ты лучший я твой фанат :) 
# Пожалуйста не бань меня
# Не находи меня по IP
# Не расстреливай меня
# Не насади меня на глобус
# Не рассказывай моей маме 😭