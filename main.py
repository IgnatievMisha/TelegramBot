import random

import telebot
from telebot import types
f = open("facts.txt","r",encoding="UTF-8")
facts = f.read().split('\n')
f.close()
t = open("thinks.txt","r",encoding="UTF-8")
thinks = t.read().split('\n')
t.close()

bot = telebot.TeleBot("6268151355:AAEG_h_DRFDsAInnc1LVfRDrs2tTyGJaYhI")
@bot.message_handler(commands=['start'])
def start(m,res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items1 = types.KeyboardButton("факт")
    items2 = types.KeyboardButton("поговорка")
    markup.add(items1)
    markup.add(items2)
    bot.send_message(m.chat.id,"натисни одну із кнопок",reply_markup=markup)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.skrip() == "Факт":
        answer = random.choice(facts)
    elif message.text.skrip()=="Приказка":
        answer = random.choice(thinks)
    bot.send_message(message.chat.id, "Усі кажуть " + message.text + " ,а ти купи слона")
bot.polling()
