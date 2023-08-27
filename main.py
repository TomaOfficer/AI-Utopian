from flask import Flask, render_template, request
import requests
import os
import markdown
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

app = Flask(__name__)

openai_api_key = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(model_name="gpt-4",
                  temperature=.2,
                  openai_api_key=openai_api_key)


def chat_with_ward(user_input):
  messages = [
      SystemMessage(
          content=
          "You are a virtual travel guide specializing in personalized guided tours. When provided with a specific location, offer historical context, interesting facts, and directions to explore the area. Limit your recommendations to three key points of interest near the given location. Use markdown to format your responses for better readability, and do not use ordered lists unless the list has more than one item. Note: Tailor the information to enrich the tourist's experience, focusing on unique and less-known facts."
      ),
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

  # convert markdown to HTML
  ward_response_html = markdown.markdown(ward_response)
  return render_template('index.html', ward_response=ward_response_html)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
