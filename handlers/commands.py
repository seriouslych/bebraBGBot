from commands.start import start_message
from commands.bebra import bebra_message
from commands.photo_id import photo_id_message, photo_id_send, photo_id_except
from commands.sticker import sticker_message, photo_stk_get, photo_stk_except
from commands.user_id import uid_message
from commands.test import test_message

from handlers.keyboards import cancel_inline

def commands(bot, base_dir):
    @bot.message_handler(commands=['start', 'help'], content_types=['text'])
    def start(message):
        start_message(bot, message)
        
    @bot.message_handler(commands=['pid'])
    def photo_id(message):
        photo_id_message(bot, message, cancel_inline)
        
    @bot.message_handler(commands=['stk'])
    def sticker(message):
        sticker_message(bot, message, cancel_inline)
        
    @bot.message_handler(commands=['uid'])
    def uid(message):
        uid_message(bot, message)
    
    @bot.message_handler(commands=['bebra'])
    def bebra(message):
        bebra_message(bot, message)
        
    @bot.message_handler(commands=['t'])
    def test(message):
        test_message(bot, message)
        
    @bot.message_handler(content_types=['text', 'photo'])
    def reply_check(message):
        if message.reply_to_message:
            replied_message = message.reply_to_message
            
            if message.reply_to_message.text == "🏞 Отправь мне изображение в ответ, чтобы узнать её ID":
                if replied_message.text:
                    if message.photo:
                        photo_id_send(bot, message)
                    else:
                        photo_id_except(bot, message)
                        
            if message.reply_to_message.text == "🏞 Отправь мне изображение в ответ, чтобы обработать её как стикер":
                if replied_message.text:
                    if message.photo:
                        photo_stk_get(bot, message, base_dir)
                    else:
                        photo_stk_except(bot, message)