import os

from commands.youtube_download.download import audio_download

def audio_dl_message(bot, message, log, base_dir):
    if len(message.text.split()) > 1:
        url = f'{message.text.split(maxsplit=1)[1]}'
        msg = bot.reply_to(message, f"⏩ Отправка как аудио {url}...", disable_web_page_preview=True)
        
        log.info(f"[@{message.from_user.username}] - Получено видео...")
        
        download = audio_download(base_dir, url, log)
        
        audio_dl_send(bot, message, log, download, msg)
        
def audio_dl_send(bot, message, log, download, msg):
    if download:
        with open(download, 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio_file)
        
        bot.edit_message_text("✅ Готово!", message.chat.id, msg.message_id)
        
        os.remove(download)
        
        log.info(f"[@{message.from_user.username}] - Аудио успешно скачано!")
    else:
        bot.edit_message_text("❌ Ошибка скачивания аудио :(\n\nиди нахуй", message.chat.id, msg.message_id)
