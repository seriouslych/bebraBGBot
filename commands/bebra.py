def bebra_message(bot, message, log):
    try:
        bebra_id = 'AgACAgIAAxkBAAIBkWYJYRHdb_2xsK9hdQS0CbLkTwSZAAK92DEbsk5ISBL38AABIzUkfwEAAwIAA3kAAzQE'
        bot.send_photo(message.chat.id, photo=bebra_id, caption='bebra')
        
        log.info(f"[@{message.from_user.username}] - Набебрил.")
    except Exception as e:
        log.exception("Ошибка отправки бебры: ", e)
