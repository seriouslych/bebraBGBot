def bebra_message(bot, message):
    try:
        bebra_id = 'AgACAgIAAxkBAAIBkWYJYRHdb_2xsK9hdQS0CbLkTwSZAAK92DEbsk5ISBL38AABIzUkfwEAAwIAA3kAAzQE'
        bot.send_photo(message.chat.id, bebra_id, caption='bebra')
    except Exception as e:
        print(f"Ошибка отправки: {e}")