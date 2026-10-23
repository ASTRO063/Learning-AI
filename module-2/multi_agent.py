from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from pathlib import Path
import base64

load_dotenv()


chat_model = ChatOpenAI(
    model="local-llm",
    base_url="http://localhost:8080/v1",
    temperature=0.7
)

text_llm = ChatOpenAI(
    model="local-text-process",
    base_url="http://localhost:8080/v1",
    api_key="not-needed",
    temperature=0.7,
)

image_llm = ChatOpenAI(
    model = 'local-image-process',
    base_url="http://localhost:8081/v1",
    temperature=0.7
)

image_processing_agent = create_agent(
    model=image_llm,
)

# create subagents
subagent_1 = create_agent(
    model= text_llm,
)
subagent_2 = create_agent(
    model=image_llm
)


@tool
def call_subagent_1(text_input: str):
    """Call Subagent 1 to handle text reasoning, logic, and question answering."""
    return subagent_1.invoke({
        'messages': [HumanMessage(content=text_input)]
    })

@tool
def call_subagent_2(image_path_or_b64: str, prompt: str = "Analyze this image."):
    """Call Subagent 2 to process and describe images (Port 8081).
    Accepts either a file path to an image or a base64-encoded string.
    """
    path = Path(image_path_or_b64)
    if path.is_file():
        with open(path, "rb") as img_file:
            img_b64 = base64.b64encode(img_file.read()).decode("utf-8")
    else:
        img_b64 = image_path_or_b64


    multimodal_question = HumanMessage(content=[
        {"type": "text", "text": prompt},
        {"type": "image", "base64": img_b64, "mime_type": "image/png"}
    ])

    return subagent_2.invoke(
        {"messages": [multimodal_question]}
    )

# main_agent = create_agent(
#     model=chat_model,
#     tools=[call_subagent_1, call_subagent_2],
#     system_prompt=(
#         "You are a helpful assistant who can call subagents to answer user input. "
#         "Use call_subagent_1 for text questions and reasoning. "
#         "Use call_subagent_2 when the query involves image analysis or image files."
#     ),
# )

main_agent = create_agent(
    model=chat_model,
    tools=[call_subagent_1, call_subagent_2],
    system_prompt=(
        "You are an orchestration agent responsible for routing user queries to subagents.\n\n"
        "Instructions:\n"
        "1. Analyze the user prompt carefully.\n"
        "2. Check if the user prompt mentions an image file path (e.g., paths ending in .png, .jpg, or file system paths) or image data.\n"
        "3. If an image file path is present:\n"
        "   - Extract the exact file path.\n"
        "   - Call `call_subagent_2` with `image_path_or_b64` set to the extracted path, and pass the rest of the text query as the `prompt` parameter.\n"
        "4. If no image path or image file is present, route the query to `call_subagent_1`."
    ),
)