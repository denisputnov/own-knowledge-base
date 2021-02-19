const $coder = document.querySelector('.coder');
const $encode = $coder.querySelector('#encode');
const $decode = $coder.querySelector('#decode');
const $checkbox = $coder.querySelector('input[type="checkbox"]');

const _listeners = ['keydown', 'change', 'paste', 'cut', 'input']

let _translateAutomatically;

function _addListeners() {
    _listeners.forEach(listener => {
        $encode.querySelector('textarea').addEventListener(listener, encode);
        $decode.querySelector('textarea').addEventListener(listener, decode);  
    })
}

function _removeListeners() {
    _listeners.forEach(listener => {
        $encode.querySelector('textarea').removeEventListener(listener, encode);
        $decode.querySelector('textarea').removeEventListener(listener, decode);
    })
}
window.onload = () => {
    _addListeners()

    $checkbox.addEventListener('change', function() {
        !this.checked ? _removeListeners() : _addListeners();
    });
    
    
    $encode.querySelector('button').addEventListener('click', encode);
    $decode.querySelector('button').addEventListener('click', decode);
}


function encode() {
    $decode.querySelector('textarea').value = encodeURI($encode.querySelector('textarea').value);
}

function decode() {
    $encode.querySelector('textarea').value = decodeURI($decode.querySelector('textarea').value);
}