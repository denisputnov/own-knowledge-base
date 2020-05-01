"""
EN: 
Bot func description in ENG

RU:
Описания функционала бота на Русском

Use    python bot.py    command to start.

Params: None

Copyright © 2020 Denis Putnov. All rights reserved.
"""
import telebot
import time
import config

from telebot import types

from service_commands import get_server_data
from service_commands import get_new_data
from service_commands import get_users_list
from service_commands import get_followers_amount
from service_commands import add_user_to_users_list
from service_commands import del_user_from_users_list


from commands import help
from commands import start

	
bot = telebot.TeleBot('config.TOKEN')


@bot.message_handler(commands=['start'])
def send_test_message(message):
	try:
		params = start.construct_message(message.chat.id)
		bot.send_message(chat_id=params.chat_id,
			text=params.text,
			parse_mode=params.parse_mode)

	except AttributeError:
		print('AttributeError: command not found.')
		bot.send_message(message.chat.id, 'Эта команда в данный момент недоступна.')


@bot.message_handler(commands=['help'])
def send_test_message(message):
	try:
		params = help.construct_message(message.chat.id)
		bot.send_message(chat_id=params.chat_id,
			text=params.text,
			parse_mode=params.parse_mode)

	except AttributeError:
		print('AttributeError: command not found.')
		bot.send_message(message.chat.id, 'Эта команда в данный момент недоступна.')

while True:
	try:
		bot.polling(none_stop=True, interval=0)
	except: 
		print('Connection failed')
		time.sleep(5)
