"""Работа с запросами и методами через функции"""
import requests
payload = {0:{"method": "GET"}, 1:{"method": "POST"}, 2:{"method": "PUT"}, 3:{"method": "DELETE"}}
actions = {'get': requests.get, 'post': requests.post, 'put': requests.put, 'delete': requests.delete}

def check_method(method_name, **kwargs):
    response = actions[method_name]("https://playground.learnqa.ru/ajax/api/compare_query_type", **kwargs)
    return response.text

for i in actions:
    for j in range(4):
        print(f'Для метода {actions[i]} с параметром {payload[j]} ответ: {check_method(method_name=i, params=payload[j])}')

