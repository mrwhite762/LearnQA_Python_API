"""Использование Токена, при долгих задачах"""
import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
answer = json.loads(response.text)["token"]

sleep_answer = json.loads(response.text)["seconds"]
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": answer})
print(response.text)
time.sleep(sleep_answer)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": answer})
print(response.text)
print(f'Результат: {json.loads(response.text)["result"]}')
