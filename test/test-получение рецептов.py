import requests

# Получение токена
url_token = 'http://127.0.0.1:8000/api/token/'
data = {
    "username": "qwe",
    "password": "123"
}
response = requests.post(url_token, json=data)
autr = response.json().get('access')

if not autr:
    print("Ошибка получения токена!")
    exit()

print(f"Токен получен: {autr}")

# Загрузка рецепта
url = "http://127.0.0.1:8000/recipe/"
headers = {
    "Authorization": f"Bearer {autr}"
}
path = '/dafg/media/avatars/vecteezy_3d-rendering-spooky-halloween_19953650_1.png'

# Открытие файла
with open(path, 'rb') as a:
    data = {
        'title': 'qwerty',
        'description': 'res',
        'instructions': 'fdwgetdwfgfdgrghgreghgfewgefeghregw',
        'ingredients': 'yhuihiuhw',
        'created_at': '2024-02-01',
        'updated_at': '2024-02-02',
    }
    files = {'photo': a}

    # Отправка запроса
    response = requests.post(url, data=data, headers=headers, files=files)
print('Обработка ответа о создании рецепта: \n')
# Обработка ответа
if response.status_code == 201:
    print(f'Создано: {response.json()}')
else:
    print(f'Ошибка: {response.status_code} {response.text}')



print('\nОбработка ответа о получении всез рецептов: \n')
# Полуыение данных о рецептаз
response = requests.get(url=url, headers=headers)
if response.status_code == 200:
    print('Получено: ', response.text)

else:
    print(f'Ошибка: {response.status_code} {response.text}')