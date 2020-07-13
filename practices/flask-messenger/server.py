from flask import Flask, request, abort
import datetime
import time

app = Flask(__name__)

messages = [
    {'username': 'Nick', 'text': 'Hello', 'time': 0.0}
]

users = {
    'Nick': '12345'
}


@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/status')
def status():
    return {
        'status': True,
        'name': 'Skillbox Messenger',
        'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route('/send', methods=['POST'])
def send():
    """
    принимаем JSON
    {
        "username": str
        "password": str
        "test": str
    }
    :return: JSON {"ok: true"}
    """
    username = request.json['username']
    password = request.json['password']

    if username in users:  # зарегистрированный пользователь
        if password != users[username]:  # авторизуем
            return abort(401)
    else:  # новый пользователь
        users[username] = password  # регистрируем, вносим в базу

    text = request.json['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)

    print(messages)

    return {'ok': True}


@app.route('/messages')
def messages_view():
    after = float(request.args.get('after'))

    # filter_messages = []
    # for message in messages:
    #     if message['time'] > after:
    #         filter_messages.append(message)

    # list comprehension
    filter_messages = [message for message in messages if message['time'] > after]

    return {
        'messages': filter_messages
    }


app.run()
