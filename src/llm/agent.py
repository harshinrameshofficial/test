from .model import ChatGroq
from langgraph.prebuilt import create_react_agent
from src.tools import tools_list

def get_agent(prompt_path='src/prompt/restrictive_prompt.txt'):
    model = ChatGroq(temperature=0, model_name="gemma2-9b-it")
    with open(prompt_path, 'r') as file:
        restrictive_prompt = file.read()
    agent = create_react_agent(
        model=model,
        tools=tools_list,
        prompt=restrictive_prompt
    )
    return agent