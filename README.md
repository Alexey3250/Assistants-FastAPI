# Асинхронный API с FastAPI и OpenAI

Суммаризирует полученную переписку с клиентом и отправляет ее обратно.

<img src="https://camo.githubusercontent.com/e8af3e348afc071756a11eec7d4877a762613a3b4eb94192c9b7babae7ea7499/68747470733a2f2f692e696d6775722e636f6d2f334e515a5244672e706e67" >

## Начало работы

Прежде всего, убедитесь, что у вас установлены Python и pip. Но, конечно, у вас они уже установлены, не так ли? Ведь кто в наши дни не использует Python!

### Установка зависимостей

Для установки этих удивительно уникальных зависимостей просто запустите:

```bash
pip install -r requirements.txt
```

Это действительно неожиданный шаг в процессе установки, верно?

### Запуск сервера

Запустите сервер, выполнив следующую магическую команду:

```bash
uvicorn main:app --reload
```

А вот и наш великолепный сервер готов к работе! О, какое волнение!

## Использование API

Для взаимодействия с API вы можете использовать любой инструмент, который отправляет HTTP-запросы. Но мы знаем, что вы выберете Postman, потому что это так оригинально.

### Пример запроса

Следующий TypeScript код покажет вам, как это делается (но, конечно, вы и сами это знаете):

```typescript
import axios from 'axios';

const response = await axios.post('http://127.0.0.1:8000/summarise/', {
    message: "Кидаем стринг со всеми сообщениями суда"
});
console.log(response.data);
```

Или, если вы предпочитаете Python (какой сюрприз!), вот пример:

```python
import requests

response = requests.post('http://127.0.0.1:8000/summarise/', json={"message": "Кидаем стринг со всеми сообщениями суда"})
print(response.json())
```

Ну и, разумеется, Postman. Просто вставьте URL и данные. Это так сложно, не правда ли?