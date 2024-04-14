import translators as ts

def translate_message(bot, message, log, lang_inline):
    bot.reply_to(message, "💬 На каком языке перевести?", reply_markup=lang_inline)
    
def translator(bot, message, log, language):
    tr_msg = f'{message.text.split(maxsplit=1)[1]}'
    
    tr_result = ts.translate_text(tr_msg, language, translator='google')
    
    bot.reply_to(message, f"{tr_result}")
    
    log.info(f"[@{message.from_user.username}] - Отправлен перевод")