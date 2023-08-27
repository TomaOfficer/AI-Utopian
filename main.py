import os
from langchain import OpenAI
from langchain.agents import Tool, load_tools, initialize_agent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}.")
prompt_template.format(adjective="funny", content="chickens")

llm = OpenAI(openai_api_key=openai_api_key,
             temperature=0,
             model_name="text-davinci-003")

llm_chain = LLMChain(llm=llm, prompt=prompt_template)

input_data = {'adjective': 'funny', 'content': 'chickens'}

# Run the chain
response = llm_chain.run(input_data)

# Print the response
print(response)
