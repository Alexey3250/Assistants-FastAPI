from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
import time

# Load the API key and Assistant ID from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
summariser_assistant_id = "asst_kCSrKaHjh589gbKr2fphQ93T"

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for the request payload
class MessageRequest(BaseModel):
    message: str

# Endpoint to process and respond to the message
@app.post("/summarise/")
async def summarise(request: MessageRequest):
    print("Starting summarisation process...")
    
    # Initialize OpenAI client with API key
    client = openai.Client(api_key=openai_api_key)

    # Create a thread
    thread = client.beta.threads.create()
    print(f"Thread created with ID: {thread.id}")

    # Add a message to the thread with the content from the request
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=request.message
    )
    print("Message added to the thread.")

    # Start the run using the Assistant ID
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=summariser_assistant_id
    )
    print(f"Run started with ID: {run.id}")

    # Function to check the run status
    def check_run_status(thread_id, run_id):
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            print(f"Run status: {run.status}")
            return run.status
        except Exception as e:
            print(f"Error retrieving run status: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    # Wait for the run to complete or timeout after 7 seconds
    start_time = time.time()
    while True:
        if time.time() - start_time > 7:
            print("Run did not complete in time.")
            raise HTTPException(status_code=500, detail="Run did not complete in time.")
        
        status = check_run_status(thread.id, run.id)
        if status == 'completed':
            print("Run completed successfully.")
            break
        elif status in ['failed', 'cancelled']:
            print(f"Run {status}.")
            raise HTTPException(status_code=500, detail=f"Run {status}")
        time.sleep(0.5)

    # Get the completed run's messages
    messages = client.beta.threads.messages.list(thread_id=thread.id)

    # Extract the assistant's last response
    for message in messages.data:
        if message.role == "assistant" and message.content:
            text_content = message.content[0].text
            if text_content:
                print("Returning the assistant's response.")
                return {"assistant_response": text_content.value}

    print("No response from the assistant.")
    raise HTTPException(status_code=500, detail="No response from the assistant")

# Run the FastAPI app with Uvicorn
# You would typically call this from the command line
# uvicorn.run(app, host="0.0.0.0", port=8000)
