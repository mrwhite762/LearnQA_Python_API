"""Работа с запросами и методами"""
import requests

payload = {0:{"method": "GET"}, 1:{"method": "POST"}, 2:{"method": "PUT"}, 3:{"method": "DELETE"}}
for i in range(4):
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload[i])
    print(f"Для метода GET с параметром {payload[i]} ответ: {response.text}")

for i in range(4):
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload[i])
    print(f"Для метода POST с параметром {payload[i]} ответ: {response.text}")

for i in range(4):
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload[i])
    print(f"Для метода PUT с параметром {payload[i]} ответ: {response.text}")

for i in range(4):
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload[i])
    print(f"Для метода DELETE с параметром {payload[i]} ответ: {response.text}")