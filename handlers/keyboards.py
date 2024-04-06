from telebot import types

# Cancel / Отмена
cancel_inline = types.InlineKeyboardMarkup()
item_cancel = types.InlineKeyboardButton(text='❌ Отмена', callback_data='cancel')
cancel_inline.add(item_cancel)