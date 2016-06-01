# Import libs
import telebot
import configparser
from random import randint

# Parse config file to get the API key
config = configparser.ConfigParser()
config.read("MagicConchShell.cfg")

TOKEN = config['telegram_bot_API']['API_TOKEN']

# Declare bot
bot = telebot.TeleBot(TOKEN)

# Message handler for /start and /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "I am the Magic Conch Shell. Ask me a Y/N question.")

# List of responses 
responses = ['Maybe someday', 'Yes', 'No', "I don't think so"]
which_one = 'Neither'
what_to_do = 'Nothing' 

# Handle the Magic Conch Shell auto question response
@bot.message_handler(regexp="(W|w)ill|(c|C)an|(D|d)oes|(m|M)ay|(i|I)s|(A|a)m|(S|s)hould")
def handle_message(message):
	length = len(responses) - 1
	myResponse = responses[randint(0,length)]
	bot.reply_to(message, myResponse)

@bot.message_handler(regexp="(w|W)hat/*/?$")
def what_to_do_message(message):
	bot.reply_to(message, what_to_do)

@bot.message_handler(regexp="(W|w)hich/*/?$")
def which_one_message(message):
	bot.reply_to(message, which_one)

# Handle the MCS inline question (MAIN WAY)
@bot.message_handler(commands=['ask'])
def ask_question(message):
	handle_message(message)

# Bot waits for events
print("MagicConchShell is running...")
bot.polling()







