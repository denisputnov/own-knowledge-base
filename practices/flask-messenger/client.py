import requests


def send_message(username, password, text):
    message = {'username': username, 'password': password, 'text': '123'}
    response = requests.post('http://127.0.0.1:5000/send', json=message)
    return response.status_code == 200


username = input('Введите имя: ')
password = input('Введите пароль: ')

while True:
    text = input('-')
    result = send_message(username, password, text)
    if result is False:
        print('Error')
