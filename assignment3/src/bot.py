# src/bot.py
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create ChatBot instance
chatbot = ChatBot(
    'TerminalBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)

# Train the chatbot with English corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
