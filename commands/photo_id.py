def photo_id_message(bot, message, cancel_inline):
    bot.reply_to(message, "🏞 Отправь мне изображение в ответ, чтобы узнать её ID", reply_markup=cancel_inline)

def photo_id_send(bot, message, log):
    pid = message.photo[-1].file_id
    bot.reply_to(message, f"ID фото: <code>{pid}</code>", parse_mode='html')
    
    log.info(f"[@{message.from_user.username}] - Узнал ID фото: '{pid}'")
    
def photo_id_except(bot, message):
    bot.reply_to(message, "Отправь мне изображение в ответ, балбес")