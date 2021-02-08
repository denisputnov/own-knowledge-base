const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
const microphone = document.querySelector('.startrecord');

recognition.lang = "ru-RU";

microphone.onclick = function() {
    recognition.start();
}

recognition.onresult = function(event) {
    document.querySelector('.container').insertAdjacentHTML('beforeend', `<p class="resstr">${event.results[0][0].transcript}</p>`)
}

recognition.onspeechend = function() {
    recognition.stop();
};