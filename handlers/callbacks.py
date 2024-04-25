def callback(bot, log):
            
    @bot.callback_query_handler(func=lambda call: True)
    def cancel(call):
        chat_id = call.message.chat.id
        message_id = call.message.message_id

        if call.data == 'cancel':
            try:
                bot.delete_message(chat_id, message_id)
            except Exception as e:
                log.exception("Ошибка при удалении сообщения:", e)
