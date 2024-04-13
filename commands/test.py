import os

from dotenv import load_dotenv

load_dotenv()

version = os.getenv('version')

def test_message(bot, message, log):
    bot.reply_to(message,
f"""
<code>TEST</code>

<i>мэнчик, щас лесной падж - это мэта плей, шаришь? 
берёшь толстозадого и пошуршал крипсов стругать. 
к 20 минуте вывозишь момчик, а там и рампага не за горами. полный АЙС!</i>

<code>bebraBGBot {version}</code>
""", parse_mode='html'
)

    log.info(f"[@{message.from_user.username}] - TEST - BebraBGBot v{version}")
