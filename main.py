from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Initialize the chat model, an instance of the ChatOpenAI class
chat = ChatOpenAI()


# Function to define prompt
def chat_with_ward(user_input):
  messages = [
      SystemMessage(content="You are a formal chatbot named Ward."),
      HumanMessage(content=user_input)
  ]
  response = chat(messages)
  return response.content


# Main function for user interaction
def main():
  print("I am Ward. Let's chat.")
  while True:
    #The input function is used to take input from the user.
    user_input = input("You: ")
    ward_response = chat_with_ward(user_input)
    print(f"Ward: {ward_response}")


if __name__ == "__main__":
  main()
