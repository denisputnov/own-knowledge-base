const $gameBoard = document.getElementById('game');
let gameBoardSize;
let now = 'cross';
let used = [];

window.onload = () => {
    gameBoardSize = $gameBoard.offsetHeight;
    console.log(gameBoardSize);
}

window.addEventListener('resize', () => {
    gameBoardSize = $gameBoard.offsetHeight;
    console.log(gameBoardSize);
})

$gameBoard.addEventListener('click', (e) => {
    add(calculateCeil(e));
})

function calculateCeil(event) {
    return { 
        x: _calculateRowIndex(event.offsetY),
        y: _calculateColumnIndex(event.offsetX),
    }
}

function _calculateColumnIndex(ofx) {
    if (ofx < gameBoardSize / 3) return 1;
    if (ofx > gameBoardSize / 3 * 2) return 3;
    return 2;
}

function _calculateRowIndex(ofy) {
    if (ofy < gameBoardSize / 3) return 1;
    if (ofy > gameBoardSize / 3 * 2) return 3;
    return 2;
}

function add(cords) {
    if (used.some(elem => (elem.x == cords.x && elem.y == cords.y))) return;
    let element = document.createElement('div')
    element.style.gridRowStart = cords.x;
    element.style.gridColumnStart = cords.y;
    element.classList.add(now);
    $gameBoard.appendChild(element);
    now == 'cross' ? now = 'circle' : now = 'cross';
    used.push(cords);
}
