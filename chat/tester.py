import requests

# URL of the FastAPI server
url = "http://127.0.0.1:8000/chat/"

# Список сообщений для отправки
messages_to_send = [
    "Я хочу поехать в дубай",
    "Хочу забронировать тур",
    "Я поеду один",
    "Какие варианты трансфера существуют?",
    "Мне нужно будет заказать такси"
]

# Инициализация переменной для ID треда
thread_id = None

# Функция для отправки сообщений и получения ответов
def send_message_get_reply(message, thread_id):
    response = requests.post(url, json={"message": message, "thread_id": thread_id})
    if response.status_code == 200:
        data = response.json()
        return data['response'], data['thread_id']
    else:
        print(f"Error: {response.text}")
        return None, thread_id

# Отправка сообщений и получение ответов
for message in messages_to_send:
    print(f"Сообщение, отправленное помощнику: {message}")
    response, thread_id = send_message_get_reply(message, thread_id)
    print(f"Ответ помощника: {response}, ID треда: {thread_id}")
