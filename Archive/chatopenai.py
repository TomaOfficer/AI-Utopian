from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Initialize the chat model, an instance of the ChatOpenAI class. Or, another way to say that, create a new variable called "chat" that is equal to a function pulled from Langchain called ChatOpenAI.
chat = ChatOpenAI()


# Function to define prompt
def chat_with_ward(user_input):
  messages = [
      SystemMessage(content="You are a formal chatbot named Ward."),
      HumanMessage(content=user_input)
  ]
  # In Python, objects can be made callable, meaning they can be used like functions. This is achieved by defining a special method called __call__ within the class. Calling chat(messages) invokes the __call__ method of the ChatOpenAI class (or similar method depending on the class implementation). This method processes the messages and returns a response object.
  response = chat(messages)
  # The return statement in a function is used to send a value back to the place where the function was called. In this case, return response.content sends the content of the response back to the caller. The content of the response is assigned to ward_response. Later, when we print ward_response, we will see the response from Ward.
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
