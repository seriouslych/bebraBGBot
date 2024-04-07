from bot_token import bot, base_dir

from handlers.commands import commands
from handlers.callbacks import callback

commands(bot, base_dir)
callback(bot)

bot.infinity_polling()
