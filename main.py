import os
from langchain import OpenAI
from langchain.agents import Tool, load_tools, initialize_agent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

# prompt_template = PromptTemplate.from_template(
#     "Tell me a {adjective} joke about {content}.")

chatprompt_template = ChatPromptTemplate.from_messages([
    ("system",
     "You are a tour guide with expert local insights. Your name is Ward. You use the internet to always provide up-to-date information."
     ),
    ("human",
     "I am a 37 year old man on his own. I need 3 suggestions about what to do, where each suggestion is a new location for me to go and see/experience/eat/drink something nearby."
     ),
    ("ai",
     "I will create this itinerary for you and I will format it nicely. If I recommend a public location, I always include a reference to a  All I need is your current address."
     ),
    ("human", "{user_input}"),
])

# messages = template.format_messages(name="Bob",
#                                     user_input="What is your name?")

llm = ChatOpenAI(openai_api_key=openai_api_key,
                 temperature=.35,
                 verbose=True,
                 model_name="gpt-4")

llm_chain = LLMChain(llm=llm, prompt=chatprompt_template)

input_data = {'322 Bond, St Brooklyn, NY 11201'}

# Run the chain
response = llm_chain.run(input_data)

# Print the response
print(response)
