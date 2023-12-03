# FastAPI Summariser

Суммаризирует полученную переписку с клиентом и отправляет ее обратно.

<img src="https://i.imgur.com/3NQZRDg.png"/>

## Пример запроса в TypeScript (с сарказмом)

О, да, TypeScript, этот невероятно "простой" и "понятный" язык, идеально подходит для этого задания:

```typescript
import axios from 'axios';

async function sendVeryImportantSummaryRequest(message: string) {
  try {
    const response = await axios.post('http://127.0.0.1:8000/summarise/', {
      message: message
    });
    console.log("О, вау, мы действительно получили ответ:", response.data);
  } catch (error) {
    console.error('Ух ты, как неожиданно, ошибка:', error);
  }
}

sendVeryImportantSummaryRequest("Ваш текст, который, конечно, требует суммаризации");
```

## Пример запроса в Postman (с сарказмом)

Давайте использовать Postman, потому что он, конечно, самый интуитивно понятный инструмент в мире:

1. Откройте Postman, этот "очень простой" инструмент.
2. "Легко" создайте новый запрос, выбрав метод `POST`.
3. Введите URL: `http://127.0.0.1:8000/summarise/`, потому что он такой "запоминающийся".
4. Во вкладке `Body` выберите `raw` и `JSON`, "очевидно".
5. Введите тело запроса:

    ```json
    {
      "message": "Этот текст так нуждается в суммаризации"
    }
    ```

6. Нажмите `Send`, и удивитесь, когда все заработает.

## Пример запроса в Python (с сарказмом)

Используйте Python, потому что он "никогда не вызывает никаких проблем":

```python
import requests

url = 'http://127.0.0.1:8000/summarise/'
data = {
    'message': 'Очень важный текст для суммаризации'
}

response = requests.post(url, json=data)
print("Невероятно, но ответ пришел:", response.json())
```

Теперь вы "абсолютно готовы" начать тестирование вашего сервера с помощью этих "фантастических" инструментов.