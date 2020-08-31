import telebot
from telebot import types

import telegram

import config
from config import *


class Bot:

    def __init__(self):
        bot = telebot.TeleBot(config.token)
        bot.remove_webhook()
        bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))
        return bot


    @bot.message_handler(commands=["start"])
    def keyboard (message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('пн', 'вт', 'ср')
        markup.row('чт', 'пт', 'сб')
        markup.row('чс/зн')
        bot.send_message(message.chat.id, "Привет!", reply_markup=markup)
