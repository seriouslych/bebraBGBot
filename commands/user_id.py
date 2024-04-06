def uid_message(bot, message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Ваш ID: <code>{user_id}</code>", parse_mode='html')