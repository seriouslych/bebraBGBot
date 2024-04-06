import telebot
import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')

bot = telebot.TeleBot(token)