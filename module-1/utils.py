from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from pprint import pprint

chat_model = ChatOpenAI(
    model="local-llm",
    base_url="http://localhost:8080/v1",
    temperature=0.7
)

agent = create_agent(
    model = chat_model
)


