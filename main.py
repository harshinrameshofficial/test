from dotenv import load_dotenv
from src.tools import tools_list
from src.llm.agent import get_agent

# Load environment variables
load_dotenv()

agent = get_agent()

def get_final_response(result):
    """Extract the final AI response from the agent result."""
    if hasattr(result, 'messages') and result.messages:
        last_message = result.messages[-1]
        if hasattr(last_message, 'content'):
            return last_message.content
    elif isinstance(result, dict) and 'messages' in result:
        messages = result['messages']
        if messages:
            last_message = messages[-1]
            if isinstance(last_message, dict) and 'content' in last_message:
                return last_message['content']
            elif hasattr(last_message, 'content'):
                return last_message.content
    return str(result)

# Continuous interaction loop
if __name__ == "__main__":
    print("Hi! I'm Maya, your AI assistant.")
    print("I can help you with:")
    print("• Personal information about me")
    print("• Current date and time") 
    print("• Weather information for any city")
    print("Feel free to say hi or ask me anything within these capabilities!")
    print("Type 'quit' to exit.")
    print("-" * 50)
   
    while True:
        try:
            user_input = input("\nYou: ").strip()
           
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
           
            if not user_input:
                continue
           
            result = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )
           
            final_response = get_final_response(result)
           
            print(f"AI Response: {final_response}")
            print("-" * 50)
           
        except KeyboardInterrupt:
            print("\n\nExiting... Goodbye!")
            break
        except Exception as e:
            print(f"\nError occurred: {e}")
            print("Please try again or type 'quit' to exit.")
            continue