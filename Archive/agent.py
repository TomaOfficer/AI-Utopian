from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)
tools = load_tools(['wikipedia'], llm=llm)

agent = initialize_agent(tools,
                         llm,
                         agent="zero-shot-react-description",
                         verbose=True)

agent.run("architect from Barcelona?")
