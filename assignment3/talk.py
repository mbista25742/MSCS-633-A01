# talk.py
import sys
import os

# src folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'src'))

from bot import chatbot

print("Type 'quit' to exit.")

while True:
    try:
        #get user input
        user_input = input("user: ")
        if user_input.lower() == 'quit':
            break
        #get output from trained chatbot model
        response = chatbot.get_response(user_input)
        print("bot:", response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
