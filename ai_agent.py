from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType,AgentExecutor,load_tools,initialize_agent
import os
#importing my openai api key (I removed my api key for privacy)
os.environ["OPENAI_API_KEY"] = ""
#creating Agent
def agent()-> AgentExecutor:
    #preparing chat model
    llm=ChatOpenAI(temperature=0.1,streaming=True)
    #tools used by agent
    tools=load_tools(llm=llm,tool_names=['wikipedia'])
    #setting agent as general purpose action agent
    return initialize_agent(llm=llm,tools=tools,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

chain=agent()

prompt = "what is the longest river in the world?"

# Getting response from the agent
response = chain.run(prompt)

# Printing the response
print("\nAgent Response:\n", response)
