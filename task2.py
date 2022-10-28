"""Подсчет колличества редиректов + их адреса"""
import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
history_response = response.history

print(f'Всего редиректов: {len(history_response)}')
for i in range(len(history_response)):
    print(response.history[i].url)

print(f'Последний редирект: {response.history[len(history_response)-1].url}')



