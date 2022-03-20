# 20-03-2022

import requests

# создаем константы, пишем в верхнем регистре
URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'MzNhZmIwMWItM2EwMy00N2ExLThiZjQtYjFlMWYwMzIxYmU5OjlhOThkMzJmN2FhNDRkY2FiZmJlM2ExNjgzOGMwMTM4'

# используем операцию конкатенации Basic + KEY
headers_auth = {'Authorization': 'Basic ' + KEY}

# для аутентификация используем метод .post из модуля requests и для именнованного аргумента headers
# передаем наш словарь headers_auth
auth = requests.post(URL_AUTH, headers=headers_auth)

# если получаем значение кода равное 200, все правильно, если 401, то програма выдаст ошибку
if auth.status_code == 200:
    # получим токен объекта auth через свойство .text
    token = auth.text

    # запускаем цикл и делаем зацикливание, чтобы пользователь мог вводить желаемое количество слов
    while True:
        # запрашиваем у пользователя ввод слова
        word = input('Пожалуйста, введите слово для перевода: ').lower()
        # если слово есть
        if word:
            # идет формирование  заголовка
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            # идет формирование get запроса
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            # отправляем в get запрос
            req = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            result = req.json()
            # пытаемся получить ответ на запрос
            try:
                print(result['Translation']['Translation'].capitalize())
            # если ловим ошибку, то
            except:
                print('Не найдено слово для перевода. Пожалуйста, попробуйте еще раз.')

# если не смогли авторизоваться, то произойдет эта ошибка
else:
    print('Error. Please, try again!')