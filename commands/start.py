import os

from dotenv import load_dotenv

load_dotenv()

version = os.getenv('version')

def start_message(bot, message):
    bot.reply_to(message,
            f"""
<code>BebraBGBot - v{version}</code>

<b>Команды бота:</b>
    /start и /help - помощь
    /pid - узнать ID фото
    /uid - узнать ID пользователя
    /bebra - бебрить
    /vid [ссылка] - скачивать видео с ютуба
    /aud [ссылка] - скачивать аудио с ютуба
    /stk - преобразование изображения в размер подходящий для стикера
            """,
                parse_mode='html')
