import os
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import AzureChatOpenAI
from tools.rainfall_check import rainfall_checking
from tools.news_summary import news_summary_tool
from tools.movie_summary import movie_summary_tool
from langchain.agents.agent_toolkits import NLAToolkit
from langchain.agents import load_tools
from dotenv import load_dotenv

load_dotenv()

def chatbot_agent(question):
    llm_openai = AzureChatOpenAI(deployment_name=os.getenv("GPT_VERSION"), temperature=0,
                                 openai_api_version=os.getenv("OPENAI_API_VERSION"))
    tools = [rainfall_checking, news_summary_tool, movie_summary_tool]
    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    agent_chain_openai = initialize_agent(tools, llm_openai, AgentType="chat-conversational-react-description",
                                          verbose=False)
    res = agent_chain_openai.run(question)
    return res
