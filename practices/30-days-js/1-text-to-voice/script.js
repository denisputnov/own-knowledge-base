function speech() {
    let text = document.querySelector('textarea').value;
    let msg = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.cancel(); // cancel speaking for bug fix
    window.speechSynthesis.speak(msg);
}

const $speechButton = document.querySelector('#speech__button');

$speechButton.addEventListener('click', speech);
