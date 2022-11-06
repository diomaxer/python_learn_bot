from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from connection import bot
from manager_db.manager import SQLManager


@bot.message_handler(commands=['start', 'next'])
def ask_question(message):
    response = SQLManager.get_question()

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Remember", callback_data='remember'),
        InlineKeyboardButton("Forgot", callback_data='forgot')
    )

    bot.send_message(message.chat.id, response, reply_markup=markup)


@bot.message_handler(commands=['settings'])
def settings(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Add question', callback_data='add_question'),
        InlineKeyboardButton('Update question', callback_data='update_question'),
    )
    bot.send_message(message.chat.id, 'Here u can manage your settings', reply_markup=markup)

