from langchain import OpenAI
from langchain.chains import LLMMathChain
import os
from langchain.agents import Tool
from langchain.agents import load_tools
from langchain.agents import initialize_agent

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key,
             temperature=0,
             model_name="text-davinci-003")

llm_math = LLMMathChain(llm=llm)

# initialize the math tool
math_tool = Tool(
    name='Calculator',
    func=llm_math.run,
    description='Useful for when you need to answer questions about math.')

tools = load_tools(['llm-math'], llm=llm)

zero_shot_agent = initialize_agent(agent="zero-shot-react-description",
                                   tools=tools,
                                   llm=llm,
                                   verbose=True,
                                   max_iterations=3)

zero_shot_agent("what is (4.5*2.1)^2.2?")
