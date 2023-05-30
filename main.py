import telebot
bot = telebot.TeleBot("6268151355:AAEG_h_DRFDsAInnc1LVfRDrs2tTyGJaYhI")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'здоров брат (☞ﾟヮﾟ)☞')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Усі кажуть " + message.text + " ,а ти купи слона")
bot.polling()