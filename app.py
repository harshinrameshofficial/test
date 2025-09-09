from langchain_groq import ChatGroq
from dotenv import load_dotenv
from datetime import datetime
from langgraph.prebuilt import create_react_agent
# Load environment variables
load_dotenv()

model = ChatGroq(temperature=0, model_name="gemma2-9b-it")

def personal_info() -> str:
    """Get personal information."""
    return "I am a helpful AI assistant."

def date_time() -> str:
    """Get the current date and time."""
    return "Current date and time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

tools_list = [personal_info, date_time, get_weather]


agent = create_react_agent(
    model=model,  
    tools=tools_list,  
    prompt="You are a helpful assistant"  
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
print(result)
