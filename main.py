from flask import Flask, render_template, request
import requests
import os
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

app = Flask(__name__)

chat = ChatOpenAI()


def chat_with_ward(user_input):
  messages = [
      SystemMessage(content="You are a formal chatbot named Ward."),
      HumanMessage(content=user_input)
  ]
  response = chat(messages)
  return response.content


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/chat', methods=["POST"])
def handle_chat():
  user_input = request.form['user_input']
  ward_response = chat_with_ward(user_input)
  return render_template('index.html', ward_response=ward_response)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
