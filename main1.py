# Использование API сервиса погоды

# Для использования был выбран сервис WeatherAPI

import requests
import os
import sys

# Функция для чтения API-ключа из файла
def read_api_key(file_path):
    if not os.path.exists(file_path):
        print(f"⚠️  Ошибка! Файл {file_path} не найден. \nПрограмма остановлена")
        sys.exit(0)  # Завершение программы с ошибкой, если файл с API-ключом не найден
    with open(file_path, 'r') as file:
        return file.read().strip()

# Функция отправки запроса на получение данных о погоде в указанном городе
def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()

# Путь к файлу с API-ключом
api_key_file = "API-key.txt"
api_key = read_api_key(api_key_file)

print(api_key)

# Хранить API-ключ в коде программы, это очень небеопасно. По этому я храню свой ключ в отдельном .txt файле
# И это очень важно продумать заранее, т.к. если запушить коммит с API-ключом, и затем разрабатывать программу - 
# то убрать его из кода в репозитории в будущем, будет уже практически невозможно

# Также нужно будет настроить файл .gitignore, но в рамках данного тестового задания я оставлю файл с API-ключом в репозитории, что бы этот проект можно было корректно запустить.

# Далее, выбираю город Екатеринбург
city = "Yekaterinburg"
weather_data = get_weather(api_key, city) # Отправляю запрос на получение данных о погоде

# Вывожу нужные данные в консоли:
print(f"Текущая температура: {weather_data['current']['temp_c']}°C")
print(f"Скорость ветра: {weather_data['current']['wind_kph']} км/ч")
print(f"Направление ветра: {weather_data['current']['wind_dir']}")
print(f"Влажность: {weather_data['current']['humidity']}%")
print("")
print(f"Данные актуальны на: {weather_data['current']['last_updated']}")




