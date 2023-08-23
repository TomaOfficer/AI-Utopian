from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

# Initialize the chat model
chat = ChatOpenAI()


# Function to translate English text to French
def translate_to_french(english_text):
  messages = [
      SystemMessage(
          content=
          "You are a helpful assistant that translates English to French."),
      HumanMessage(content=english_text)
  ]
  response = chat(messages)
  return response.content


# Main function for user interaction
def main():
  print("Welcome to the English to French Translator!")
  while True:
    english_text = input("Enter a sentence in English (or 'quit' to exit): ")
    if english_text.lower() == 'quit':
      break
    french_translation = translate_to_french(english_text)
    print(f"French Translation: {french_translation}")


if __name__ == "__main__":
  main()
