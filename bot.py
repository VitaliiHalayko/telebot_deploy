import telebot

API_TOKEN = '8017539047:AAFeluV9WTOOYigQrZjeQl7GvKkISHCtWZ0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to the bot! How can I assist you today?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "You said: " + message.text)

if __name__ == '__main__':
	print("Bot is polling...")
	bot.polling(none_stop=True)