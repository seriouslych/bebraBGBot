from bot_token import bot, base_dir
from log.logger import log

from handlers.commands import commands
from handlers.callbacks import callback

log.info("BebraBGBot запущен...")

commands(bot, base_dir, log)
callback(bot)

bot.infinity_polling()
