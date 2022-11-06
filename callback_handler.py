from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from connection import bot
from manager_db.manager import SQLManager


@bot.callback_query_handler(func=lambda call: call.data in ('add_question', 'update_questions'))
def add_question(call):
    if call.data == 'add_question':
        msg = bot.send_message(call.message.chat.id, 'Write new question below')
        bot.register_next_step_handler(msg, get_question)


def get_question(message):
    msg = bot.send_message(message.chat.id, 'Write answer below')
    bot.register_next_step_handler(msg, get_answer, message.text)


def get_answer(message, text):
    question = text
    answer = message.text
    SQLManager.create_question(question, answer)
    bot.send_message(message.chat.id, f'Added question:\n{question}\n\nAdded answer:\n{answer}')


@bot.callback_query_handler(func=lambda call: call.data in ('remember', 'forgot'))
def call_back(call):
    markup = InlineKeyboardMarkup()
    if call.data == 'remember':
        markup.add(InlineKeyboardButton("Excellent", callback_data='excellent'))

    elif call.data == 'forgot':
        response = SQLManager.get_current_question(question=call.message.text)
        markup.add(InlineKeyboardButton(response[0], callback_data='answer'))

    bot.edit_message_text(call.message.text, reply_markup=markup, chat_id=call.message.chat.id,
                              message_id=call.message.message_id)