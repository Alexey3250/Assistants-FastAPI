import requests
import concurrent.futures
import json
import time

# The endpoint of your FastAPI server
URL = "http://127.0.0.1:8000/summarise/"

# Example request data
data = {
    "message": "User Привет ИИ - Консьерж Здравствуйте! Как я могу помочь вам сегодня? User Мне нужно поехать в дубай ИИ - Консьерж Отличный выбор! Дубай - замечательное место для путешествия. Это будет тур или вы заинтересованы в бронировании отдельных услуг?\n\nUser Тур\n\nИИ - Консьерж Прекрасно! Для начала, могли бы вы уточнить, на какие даты вы планируете поездку в Дубай? И насколько долго вы хотели бы там остаться?\n\nUser на 1 день на новый год, мне нравится стоять в пробке чтобы посмотреть фейерверк\n\nИИ - Консьерж Поездка в Дубай на Новый год звучит восхитительно! Для более точного подбора тура мне нужно знать, сколько вас будет взрослых и есть ли среди путешественников дети? Если есть дети, сообщите, пожалуйста, их возраст.\n\nUser 1 взрослый\n\nИИ - Консьерж Отлично, спасибо за информацию. Могу я узнать, предпочитаете ли вы прямой трансфер в отель после прибытия в Дубай?\n\nUser прямой трансфер из москвы, отель без разницы какой, нужно такси до отеля\n\nИИ - Консьерж Понял вас. Рассматривая ваши предпочтения, последний вопрос: есть ли у вас определённые пожелания к аэропорту вылета из Москвы?\n\nUser нет\n\nИИ - Консьерж Хорошо, я собрал всю необходимую информацию для составления вашего тура в Дубай на Новый год. Спасибо за ваш запрос, я передам его нашей команде, и наши специалисты свяжутся с вами в ближайшее время. Как вам будет удобнее получить обратную связь: по телефону или электронной почте?\n\nUser По телефону +971 69420395\n\nИИ - Консьерж Спасибо за предоставленную информацию. Мы свяжемся с вами по указанному телефону +971 69420395 для уточнения деталей и подтверждения вашего тура в Дубай. Если у вас возникнут вопросы до этого времени, не стесняйтесь обращаться. Хорошего вам дня!"
    # Rest of your message content
}

# Function to send a POST request and measure time taken
def send_request(request_number):
    start_time = time.time()  # Start time
    print(f"Request {request_number} sent at {time.strftime('%X')}")

    try:
        response = requests.post(URL, json=data)
        response_json = response.json()
    except Exception as e:
        response_json = {"error": str(e)}

    end_time = time.time()  # End time
    time_taken = end_time - start_time  # Calculate time taken

    print(f"Response for request {request_number} received at {time.strftime('%X')}, Time Taken: {time_taken} seconds")
    return response_json

# Number of concurrent requests
REQUEST_COUNT = 10

# Using ThreadPoolExecutor to send requests concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(send_request, i): i for i in range(1, REQUEST_COUNT + 1)}
    for future in concurrent.futures.as_completed(futures):
        request_number = futures[future]
        result = future.result()
        print(f"Result for Request {request_number}: {result}")

# Main program end
print("All requests completed")
