# Import libs
import telebot
import configparser
import random
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
from chatterbot.training.trainers import ListTrainer

# Parse config file to get the API key
config = configparser.ConfigParser()
config.read("chatmigo.cfg")

TOKEN = config['telegram_bot_API']['API_TOKEN']

# Declare bot
bot = telebot.TeleBot(TOKEN)

# Message handler for /start and /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "I am chatmigo.")

# Set the frequency for message sending
frequency = 0.9

# Chatbot instance
chatbot = ChatBot("Stark")

# Train Listener
chatbot.set_trainer(ChatterBotCorpusTrainer)

# Words to train
chatbot.train("chatterbot.corpus.english.conversations")

# Bot action responding
@bot.message_handler(func=lambda m:(random.random() < frequency))
def chatterbot_us(message):
	response = chatbot.get_response(message)
	# Send a message in group
	bot.send_message(message.chat.id, response)

# Bot waits for events
print("Chatmigo is running...")
bot.polling()

