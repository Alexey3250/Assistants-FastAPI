import requests
import time

# URL of the FastAPI server
URL = "http://127.0.0.1:8000/chat"

# List of messages to send
messages = [
    "Hello, can you help me with a trip to Dubai?",
    "I'm interested in a tour package.",
    "I plan to travel for one day on New Year's Eve.",
    "Can you suggest some activities there?"
]

# Function to send a message and receive a response
def send_message(message, thread_id=None):
    payload = {"message": message, "thread_id": thread_id}
    try:
        response = requests.post(URL, json=payload, timeout=10)
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out after 10 seconds")
        return "fail"
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON from response")
        return "fail"


# Send the first message and receive a new thread ID
response = send_message(messages[0])
thread_id = response["thread_id"]
print(f"Response: {response['response']}, Thread ID: {thread_id}")

# Send subsequent messages using the received thread ID
for message in messages[1:]:
    time.sleep(2)  # Optional delay between messages
    response = send_message(message, thread_id)
    print(f"Response: {response['response']}, Thread ID: {thread_id}")
