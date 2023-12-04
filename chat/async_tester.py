import requests
import concurrent.futures
import time

# URL of the FastAPI server
url = "http://127.0.0.1:8000/chat/"

# Function for sending a message and receiving a reply
def send_message_get_reply(message, thread_id):
    start_time = time.time()
    response = requests.post(url, json={"message": message, "thread_id": thread_id})
    end_time = time.time()
    elapsed_time = end_time - start_time

    if response.status_code == 200:
        data = response.json()
        return data['response'], data['thread_id'], elapsed_time
    else:
        print(f"Error: {response.text}")
        return None, thread_id, elapsed_time

# Function to handle an entire conversation
def handle_conversation(messages):
    thread_id = None
    for message in messages:
        print(f"Sending message: '{message}'")
        response, thread_id, time_taken = send_message_get_reply(message, thread_id)
        print(f"Received response: '{response}' | Thread ID: {thread_id} | Time taken: {time_taken:.2f} seconds")

# Conversations
conversation1 = [
    "Я хочу поехать в дубай",
    "Хочу забронировать тур",
    "Я поеду один"
]

conversation2 = [
    "Какие варианты трансфера существуют?",
    "Мне нужно будет заказать такси",
    "Какие отели вы можете предложить?"
]

conversation3 = [
    "Я хочу поехать в Париж",
    "Ищу романтический тур",
    "Какие экскурсии включены?"
]

conversation4 = [
    "Интересуюсь поездкой в Японию",
    "Можно ли включить посещение храмов?",
    "Какие варианты проживания?"
]

conversation5 = [
    "Хочу тур в Нью-Йорк",
    "Нужны билеты на Бродвей",
    "Рекомендуйте хорошие рестораны"
]

# Running all conversations concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(handle_conversation, conversation)
        for conversation in [conversation1, conversation2, conversation3, conversation4, conversation5]
    ]
    concurrent.futures.wait(futures)
