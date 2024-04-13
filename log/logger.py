import logging
import sys
from bot_token import base_dir

logging.basicConfig(level=logging.INFO, filename=f'{base_dir}/log/bot.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='a')

log = logging.getLogger('bot')

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

log.addHandler(console_handler)
