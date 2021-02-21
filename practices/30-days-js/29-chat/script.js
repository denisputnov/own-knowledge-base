class Message {
    constructor(text, time, type) {
        this.text = text;
        this.time = time; 
        this.type = type;
    }
}

class InputMessage extends Message {
    constructor(text) {
        let _date = new Date();
        super(text, `${_date.getHours()}:${_date.getMinutes()}:${_date.getSeconds()}}`, 'input-message');
    }
}

class OutputMessage extends Message {
    constructor(text) {
        let _date = new Date();
        super(text, `${_date.getHours()}:${_date.getMinutes()}:${_date.getSeconds()}}`, 'output-message');
    }
}

function _addMessage(message) {
    $messages.insertAdjacentHTML('beforeend', `<div class="message ${message.type}">${message.text}</div>`);
}

const $chat = document.getElementById('chat');
const $input = $chat.querySelector('.chat__message-input');
const $sendButton = $chat.querySelector('.chat__send-button');
const $user = $chat.querySelector('.topbar__toggle-user');
const $messages = $chat.querySelector('#messages');

let _currentUser = 'second-user';

$user.addEventListener('click', () => {
    $user.classList.toggle('first-user');
    $user.classList.toggle('second-user');
    _currentUser === 'second-user' ? _currentUser = 'first-user' : _currentUser = 'second-user';
});

$sendButton.addEventListener('click ', _sendMessage);
window.addEventListener('keydown', (e) => {
    if (e.keyCode === 13) _sendMessage();
}) 

function _sendMessage() {
    let _messageText = $input.value.trim();
    if (_messageText === '') return; 
    $input.value = '';
    if (_currentUser ===  'second-user') return _addMessage(new OutputMessage(_messageText));
    _addMessage(new InputMessage(_messageText));
}