# React AI Agent with LangGraph

A simple implementation of a React AI agent using LangGraph and FastAPI. This agent demonstrates how to create a thinking process with reflection using LangGraph's workflow capabilities.

## Features

- React-style agent with thought generation and reflection
- FastAPI backend with RESTful endpoints
- Easy to extend with additional reasoning steps
- Built with LangGraph and LangChain

## Prerequisites

- Python 3.8+
- OpenAI API key

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your API key:
   ```
   GROQ_API_KEY=your-api-key-here
   ```

## Running the Application

Start the FastAPI server:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /chat` - Send a message to the AI agent
  - Request body: `{"message": "Your message here"}`
  - Response: `{"response": "AI's response"}`

- `GET /health` - Health check endpoint
  - Response: `{"status": "healthy"}`

## Example Usage

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the capital of France?"}'
```

## Project Structure

- `app.py` - Main application file with FastAPI setup and agent logic
- `requirements.txt` - Python dependencies