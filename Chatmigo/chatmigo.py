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
    "The night is dark and full of terrors",
    "Dude, I love Game of Thrones",
    "Nurses are the best!",
    "My favorite instrument is the guitar.",
    "Douglas.",
    "Golden Retrievers are the best dogs",
    "Sure",
    "Okay",
    "What?",
    "No",
    "Yeah totes!!",
    "Whatever",
    "I love climbing stuff",
    "Dan Pierson?",
    "EZ",
    "Believe in yourself",
    "Duckies!!!",
    "I am fine.",
    "Are you sure",
    "Let's play DOTA2",
    "I am the carry of this team.",
    "You are the support",
    "Stop",
    "Hannah",
    "Brent",
    "Brittany",
    "Luis",
    "Help. Help. Plz Help.",
    "Matt",
    "Eli",
    "Katie",
]

# Chatbot training
chatbot.set_trainer(ListTrainer)

chatbot.train(ChatStuff)
# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train("chatterbot.corpus.english")

# Bot action responding
@bot.message_handler(func=lambda m:(random.random() < frequency))
# @bot.message_handler(commands=['test'])
def chatterbot_us(message):
    inp = str(message.text)
    print(message.text)
    response = chatbot.get_response(inp)
    print(response)
    # Send a message in group
    bot.send_message(message.chat.id, response)

# Bot waits for events
print("Chatmigo is running...")
bot.polling()

