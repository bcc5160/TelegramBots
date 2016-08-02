import telebot
import configparser

# Parse config file to get the API Key
config = configparser.ConfigParser()
config.read("tattle_bot.cfg")

TOKEN = config['telegram_bot_api']['telegram_token']

# Declare bot
bot = telebot.TeleBot(TOKEN)
 
# List of users
# bot.users.getUsers();

# Get the guilty person
def tattle():
    print(bot.get_chat())


# Message handler for /start and /help
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Ask me who did it. I know.")

# Ask bot who did it
@bot.message_handler(regexp="(Who|who)")
def handle_message(message):
    tattle()
    bot.reply_to(message, "Person")

# Bot waits for events
print("Tattle_bot is running...")
bot.polling()
