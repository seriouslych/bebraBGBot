from bot_token import bot

from handlers.commands import commands
from handlers.callbacks import callback

commands(bot)
callback(bot)

bot.infinity_polling()
