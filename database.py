from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["justice_chatbot"]
chat_history = db["chat_history"]

def save_chat(user_input, bot_response):
    chat_history.insert_one({"user": user_input, "bot": bot_response})
