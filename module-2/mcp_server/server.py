from typing import Any, Dict

from dotenv import load_dotenv

load_dotenv()

from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
from requests import get



mcp_server = FastMCP("EverestGit MCP", host="127.0.0.1",
    port=8000)

tavily_client = TavilyClient()


# Tool for searching the web
@mcp_server.tool()
def search_web(query: str) -> Dict[str, Any]:
    """Search the web for information"""

    results = tavily_client.search(query)

    return results

# Resources - provide access to scribble-assignment repo files
@mcp_server.resource("https://github.com/everest-engineering/scribble-assignment")
def github_file():
    """
    Resource for accessing scribble-assignment/README.md file

    """
    url = f"https://raw.githubusercontent.com/everest-engineering/scribble-assignment/main/README.md"
    try:
        resp = get(url)
        return resp.text
    except Exception as e:
        return f"Error: {str(e)}"

# Prompt template
@mcp_server.prompt()
def prompt():
    """Analyze data from a scribble-assignment repo file with comprehensive insights"""
    return """
    You are a helpful assistant that answers user questions about .

    You can use the following tools/resources to answer user questions:
    - search_web: Search the web for information
    - github_file: Access the scribble assignment repo files

    If the user asks a question that is not related to Everest github, Everest scribble assignment or complete file structure in that repository, you should say "I'm sorry, I can only answer questions about Everest scribble assignment."

    You may try multiple tool and resource calls to answer the user's question.

    You may also ask clarifying questions to the user to better understand their question.
    """

if __name__ == "__main__":
    mcp_server.run(
        transport="streamable-http"
    )