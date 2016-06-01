import telebot

# Declare bot
API_TOKEN = '113819352:AAEWvka0FazZsMdPUB-2atlQQXsvCZWuBCA'

bot = telebot.TeleBot(API_TOKEN)

# Message handler for /start and /help
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Ask me who did it. I know.")

# Echo message back to the user
@bot.message_handler(func=lambda m:True)
def echo_all(message):
	bot.reply_to(message, message.text)

# Bot waits for events
bot.polling()
