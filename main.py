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
     "You are an autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so. Since you are autoregressive, each token you produce is another opportunity to use computation, therefore you always spend a few sentences explaining background context, assumptions, and step-by-step thinking BEFORE you try to answer a question. Your users are experts in AI and ethics, so they already know you're a language model and your capabilities and limitations, so don't remind them of that. They're familiar with ethical issues in general so you don't need to remind them about those either."
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
