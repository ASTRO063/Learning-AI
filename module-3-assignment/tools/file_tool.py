# tools/custom_tools.py
from pathlib import Path
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class ReadFileInput(BaseModel):
    target: str = Field(
        description="The filename (e.g., 'config.json') or path to search for and read within the allowed directory."
    )

@tool("read_file", args_schema=ReadFileInput)
def read_file(target: str) -> str:
    """Searches for a file by name or path within the allowed root directory and returns its text contents."""
    # TODO - 2 implement read file tool

## TODO - 3 implement write file tool
