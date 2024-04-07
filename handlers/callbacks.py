def callback(bot):
    @bot.callback_query_handler(func=lambda callback: True)
    def cancel(callback):
        chat_id = callback.message.chat.id
        message_id = callback.message.message_id

        if callback.data == 'cancel':
            try:
                bot.delete_message(chat_id, message_id)
            except Exception as e:
                print("[ОШИБКА] Ошибка при удалении сообщения:", e)