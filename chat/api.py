from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
import time

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for request data
class MessageRequest(BaseModel):
    message: str
    thread_id: str | None = None  # Optional thread ID

# Load OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

# Function to send message and get reply
def send_message_get_reply(message, thread_id=None):
    client = openai.Client()
    assistant_id = "asst_CjvyFIeraCLKB8NTAqF0FhqG"  # Your assistant ID

    if thread_id is None:
        thread = client.beta.threads.create()
        thread_id = thread.id

    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id).status
        if run_status == 'completed':
            break
        elif run_status in ['failed', 'cancelled']:
            return None, thread_id
        time.sleep(0.5)

    messages = client.beta.threads.messages.list(thread_id=thread_id).data
    last_message = next(
        (m.content[0].text.value for m in messages if m.role == "assistant" and m.content),
        None
    )

    return last_message, thread_id

# Endpoint to process message
@app.post("/chat/")
async def chat(request: MessageRequest):
    response, thread_id = send_message_get_reply(request.message, request.thread_id)
    if response is None:
        raise HTTPException(status_code=500, detail="Failed to get a response from the assistant")
    return {"response": response, "thread_id": thread_id}

# Run the FastAPI app with Uvicorn
# You would typically call this from the command line
# uvicorn.run(app, host="0.0.0.0", port=8000)
