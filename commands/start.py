import os

from dotenv import load_dotenv

load_dotenv()

version = os.getenv('version')

def start_message(bot, message, log):
    bot.reply_to(message,
            f"""
<code>BebraBGBot - v{version}</code>

<b>Команды бота:</b>
    /start и /help - помощь
    /pid - узнать ID фото
    /uid - узнать ID пользователя
    /bebra - бебрить
    /tr - перевести текст с любого языка на русский
    /sl - ухудшить качество изображения
    /stk - преобразование изображения в размер подходящий для стикера
    /vid [ссылка] - скачивание видео с YouTube
    /aud [ссылка] - скачивание видео с YouTube как аудио (в mp3)
            """,
                parse_mode='html')
    
    log.info(f"[@{message.from_user.username}] - Запустил бота / Использовал помощь")
