# Import libs
import telebot
import configparser
import random
from chatterbot import ChatBot
from chatterbot.training.trainers import ListTrainer
from chatterbot.training.trainers import ChatterBotCorpusTrainer

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
chatbot = ChatBot(
    "Steven",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.adapters.output.OutputFormatAdapter",
    database="./database.json"
)

ChatStuff = [
    "Winter is coming",
    "Pokemon GO",
    "Douglas",
    "What",
    "i believe in you"
]

# Chatbot training
# chatbot.set_trainer(ListTrainer)
chatbot.set_trainer(ChatterBotCorpusTrainer)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")
# chatbot.train(ChatStuff)
# Train based on english greetings corpus
# chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
# chatbot.train("chatterbot.corpus.english.conversations")


# Bot action responding
@bot.message_handler(func=lambda m:(random.random() < frequency))
# @bot.message_handler(commands=['test'])
def chatterbot_us(message):
    inp = str(message)
    response = chatbot.get_response(inp)
    print(response)
    # Send a message in group
    bot.send_message(message.chat.id, response)

# Bot waits for events
print("Chatmigo is running...")
bot.polling()

