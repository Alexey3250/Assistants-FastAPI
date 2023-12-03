
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

# Initialize FastAPI app
app = FastAPI()

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Pydantic model for request payload
class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None

# Pydantic model for response payload
class ChatResponse(BaseModel):
    thread_id: str
    response: str

# Endpoint to process chat messages
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    client = openai.Client()

    # Create a new thread if thread_id is None
    if request.thread_id is None:
        thread = await client.beta.threads.create()
        thread_id = thread.id
    else:
        thread_id = request.thread_id

    # Send message to OpenAI
    await client.beta.threads.messages.create(
        thread_id=thread_id, 
        role="user", 
        content=request.message
    )

    # Start and wait for the run to complete
    run = await client.beta.threads.runs.create(thread_id=thread_id, assistant_id="asst_CjvyFIeraCLKB8NTAqF0FhqG")
    # Implement logic to wait for run to complete and check status

    # Retrieve the assistant's last response
    messages = await client.beta.threads.messages.list(thread_id=thread_id)
    last_message = next(
        (m.content[0].text.value for m in messages.data if m.role == "assistant" and m.content),
        "No response"
    )

    return ChatResponse(thread_id=thread_id, response=last_message)
