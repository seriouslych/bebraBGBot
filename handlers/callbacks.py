from checkers import waiting_for_pid

def callback(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def cancel(callback):
        chat_id = callback.message.chat.id
        message_id = callback.message.message_id

        if callback.data == 'cancel':
            try:
                bot.delete_message(chat_id, message_id)
                if chat_id in waiting_for_pid:
                    waiting_for_pid[chat_id] = False
            except Exception as e:
                print("[ОШИБКА] Ошибка при удалении сообщения:", e)