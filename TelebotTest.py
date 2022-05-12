import telebot

import time


bot = telebot.TeleBot("5246096403:AAGagrEEsLu4IKj7cDZmV9YZ11s_cNIrmjA")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['time'])
def start(message):
    bot.send_message(message.chat.id, time.asctime())


@bot.message_handler(func=lambda message: True)
def lalala(message):
    age = message.text
    bot.send_message(message.chat.id, 'Сам ты ' + str(age))


bot.polling(none_stop=True)
