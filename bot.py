import telebot

bot = telebot.TeleBot("870336394:AAE_gfsjKE9AN6STu0VbQm1gSyS8vpW6YkU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)
	
bot.polling(none_stop = True)
