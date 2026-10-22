
from langchain.agents.middleware import HumanInTheLoopMiddleware
from tools import all_tools

def build_risk_based_hitl(all_tools):
    return {tool.name: True for tool in all_tools}

middlewares=[
        HumanInTheLoopMiddleware(
            interrupt_on=build_risk_based_hitl(all_tools),
            description_prefix="Tool execution requires approval",
        ),
    ]