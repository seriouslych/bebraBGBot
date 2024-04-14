from telebot import types

# Cancel / Отмена
cancel_inline = types.InlineKeyboardMarkup()
item_cancel = types.InlineKeyboardButton(text='❌ Отмена', callback_data='cancel')
cancel_inline.add(item_cancel)

# Lang / Языки - Russian / English / Belarus / Serb / Chtrad / Chsimp / German / Romanian / Ukranian / Spain
lang_inline = types.InlineKeyboardMarkup()

russian_lang = types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='russian')
english_lang = types.InlineKeyboardButton(text='🇺🇸 Английский', callback_data='english')
belarus_lang = types.InlineKeyboardButton(text='🇧🇾 Белорусский', callback_data='belarus')
serb_lang = types.InlineKeyboardButton(text='🇷🇸 Сербский', callback_data='serb')
chtrad_lang = types.InlineKeyboardButton(text='🇨🇳 Кит. Традиционный', callback_data='chtrad')
chsimp_lang = types.InlineKeyboardButton(text='🇨🇳 Кит. Упрощённый', callback_data='chsimp')
german_lang = types.InlineKeyboardButton(text='🇩🇪 Немецкий', callback_data='german')
romanian_lang = types.InlineKeyboardButton(text='🇷🇴 Румынский', callback_data='romanian')
ukranian_lang = types.InlineKeyboardButton(text='🇺🇦 Украинский', callback_data='ukranian')
spain_lang = types.InlineKeyboardButton(text='🇪🇸 Испанский', callback_data='spain')

lang_inline.add(russian_lang,
                english_lang,
                belarus_lang, 
                serb_lang, 
                chtrad_lang,
                chsimp_lang,
                german_lang,
                romanian_lang,
                ukranian_lang,
                spain_lang)