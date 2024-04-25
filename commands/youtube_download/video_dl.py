import os

from commands.youtube_download.download import video_download

def video_dl_message(bot, message, log, base_dir):
    if len(message.text.split()) > 1:
        url = f'{message.text.split(maxsplit=1)[1]}'
        msg = bot.reply_to(message, f"⏩ Отправка {url}...", disable_web_page_preview=True)
        
        log.info(f"[@{message.from_user.username}] - Получено видео...")
        
        download = video_download(base_dir, url, log)
        
        video_dl_send(bot, message, log, download, msg)
        
def video_dl_send(bot, message, log, download, msg):
    if download:
        with open(download, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file, supports_streaming=True, width=1920, height=1080)
        
        bot.edit_message_text("✅ Готово!", message.chat.id, msg.message_id)
        
        os.remove(download)
        
        log.info(f"[@{message.from_user.username}] - Видео успешно скачано!")
    else:
        bot.edit_message_text("❌ Ошибка скачивания видео :(\n\nиди нахуй", message.chat.id, msg.message_id)