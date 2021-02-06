document.querySelector('.counter__button').addEventListener('click', () => {
    const _text = document.querySelector('.counter__textarea').value.trim(); 
    document.querySelector('.counter__header').innerHTML = `Symbols: ${_text.length}, words: ${_text.split(' ').length}`;
});