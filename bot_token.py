import telebot
import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')

bot = telebot.TeleBot(token)

base_dir = os.path.dirname(os.path.abspath(__file__))