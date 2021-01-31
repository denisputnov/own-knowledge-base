let data = [
    {
        "question": "2+1",
        "ansvers": [
            {
                "text": "3",
                "isCorrect": true
            },
            {
                "text": "4",
                "isCorrect": false
            },
            {
                "text": "2",
                "isCorrect": false
            },
            {
                "text": "-1",
                "isCorrect": false
            },
        ]
    },
    {
        "question": "4+3",
        "ansvers": [
            {
                "text": "3",
                "isCorrect": false
            },
            {
                "text": "7",
                "isCorrect": true
            },
            {
                "text": "2",
                "isCorrect": false
            },
            {
                "text": "11",
                "isCorrect": false
            },
        ]
    },
    {
        "question": "14+8",
        "ansvers": [
            {
                "text": "26",
                "isCorrect": false
            },
            {
                "text": "18",
                "isCorrect": false
            },
            {
                "text": "24",
                "isCorrect": false
            },
            {
                "text": "22",
                "isCorrect": true
            },
        ]
    }
];

const $game = document.querySelector('.game');
let $buttons = $game.querySelectorAll('.game__button');
let $question = $game.querySelector('.game__question');

let _currentQuestion = 0;
let _currentScore = 0;

const update = (event) => {
    if (_currentQuestion > 0 && event.target) {
        if(event.target.dataset.isCorrect == 'true') {
            _currentScore++;
            console.log(`CurrentScore: ${_currentScore}`);
        }
    }
    if (_currentQuestion == data.length) {
        showResults();
        return;
    }

    for (let i = 0; i < $buttons.length; i++) {
        $buttons[i].textContent = data[_currentQuestion].ansvers[i].text;
        $buttons[i].dataset.isCorrect = data[_currentQuestion].ansvers[i].isCorrect;
    }
    $question.textContent = data[_currentQuestion].question
    
    _currentQuestion++;
    console.log(_currentQuestion);
}

const showResults = () => {
    for (let $button of $buttons) {
        $button.style.display = 'none';
    }
    $question.textContent = `Your result is ${_currentScore}/${data.length} !`
}

window.onload = function() {
    update();
    for (let button of $buttons) {
        button.addEventListener('click', (event) => update(event));
    }
};