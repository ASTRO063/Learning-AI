from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from pprint import pprint

from typing import Any, Dict
from langchain.tools import tool
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool()
def search_web(query: str) -> Dict[str, Any]:
    """Search the web for information"""

    results = tavily_client.search(query)

    return results

chat_model = ChatOpenAI(
    model="local-llm",
    base_url="http://localhost:8080/v1",
    temperature=0.7
)

agent = create_agent(
    model = chat_model,
    tools= [search_web]
)


