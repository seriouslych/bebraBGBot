from commands.translate import translator

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
                
    def lang(call):
        message = call.message
        
        if call.data == 'russian':
            language = 'ru'
            translator(bot, message, log, language)
            
        if call.data == 'english':
            language = 'en'

        if call.data == 'belarus':
            language = 'be'
            
        if call.data == 'serb':
            language = 'sr'
            
        if call.data == 'chtrad':
            language = 'zh-TW'

        if call.data == 'chsimp':
            language = 'zh-CN'
            
        if call.data == 'german':
            language = 'es'
            
        if call.data == 'spain':
            language = 'es'
            
        if call.data == 'romanian':
            language = 'ro'
            
        if call.data == 'ukranian':
            language = 'uk'
        