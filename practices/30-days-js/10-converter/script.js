const units = {
    'millimeters': 1,
    'centimeters': 10,
    'decimeters': 100,
    'meters': 1000,
    'kilometers': 1000000,
}

let _first = 'millimeters';
let _second = 'millimeters';

document.querySelector('.converter').querySelectorAll('select').forEach(selector => {
    selector.addEventListener('change', (e) => {
        e.target.id == 'first' ? _first = e.target.value : _second = e.target.value;
        calculateResult();
    })
})

document.querySelector('.converter').querySelector('input').addEventListener('input', calculateResult);

function calculateResult() {
    let $res = document.querySelector('.converter__result'); 
    let number = parseFloat(document.querySelector('.converter').querySelector('input').value);

    if (Number.isNaN(number)) return $res.innerHTML = "Something went wrong. Probably number is not found";

    $res.innerHTML = units[_first] / units[_second] * number;
}