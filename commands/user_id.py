def uid_message(bot, message, log):
    user_id = message.from_user.id
    bot.reply_to(message, f"Ваш ID: <code>{user_id}</code>", parse_mode='html')
    
    log.info(f"[@{message.from_user.username}] - Узнал свой ID: '{user_id}'")