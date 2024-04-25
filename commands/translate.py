import translators as ts

def translate_message(bot, message, log):
    tr_msg = f'{message.text.split(maxsplit=1)[1]}'
    
    tr_result = ts.translate_text(tr_msg, to_language='ru', translator='google')
    
    bot.reply_to(message, f"{tr_result}")
    
    log.info(f"[@{message.from_user.username}] - Отправлен перевод")