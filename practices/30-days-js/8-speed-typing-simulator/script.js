const $simulator = document.querySelector('.simulator');
const $time = $simulator.querySelector('.simulator__time');
const $done = $simulator.querySelector('.simulator__done');
const $header = $simulator.querySelector('.simulator__header');
const $input = $simulator.querySelector('.simulator__input');

let words = [
    'this',
    'push',
    'only',
    'test',
    'press',
    'key',
    'javascript',
];

let _nowWordId = randomInteger(0, words.length - 1);
$header.innerHTML = words[_nowWordId];

let _isFirstEnter = true;

let startTime;

console.log(_nowWordId);

$input.addEventListener('keydown', (e) => {
    if (e.key === " " || e.key === "Enter") {
        if ($input.value.trim() === '') return;

        if (_isFirstEnter) {
            startTime = new Date().getTime();
            _isFirstEnter = false;
        }
        
        let _word = $input.value;
        
        let _doneWord = document.createElement('div');
        _doneWord.innerHTML = _word;
        _doneWord.classList.add(_word === words[_nowWordId] ? 'correct' : 'incorrect');
         
        $done.appendChild(_doneWord);
        
        $input.value = '';
        
        words = words.filter(word => word != words[_nowWordId]);
        _nowWordId = randomInteger(0, words.length - 1);
        $header.innerHTML = words[_nowWordId];
        
        console.log(words);
        console.log(_nowWordId);


        if (words.length === 0) return endGame();
    }
});

function endGame() {
    let endTime = new Date().getTime();
    console.log('END END END');
    let score = $done.querySelectorAll('.correct').length;

    $header.innerHTML = `Your time is ${(endTime - startTime) / 1000} sec.; Your score is ${score}`
}

function randomInteger(min, max) {
    let rand = min + Math.random() * (max + 1 - min);
    return Math.floor(rand);
}