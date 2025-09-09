from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AIModel:
    def __init__(self, model_name: str, temperature: float = 0):
        self.model = ChatGroq(temperature=temperature, model_name=model_name)

    def generate_response(self, user_input: str):
        # Logic to generate a response using the model
        result = self.model.invoke({"messages": [{"role": "user", "content": user_input}]})
        return self.extract_final_response(result)

    @staticmethod
    def extract_final_response(result):
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
        return str(result)  # Fallback to string conversion