const $pad = document.querySelector('#pad');
const $input = $pad.querySelector('input');
const $numberKeys = $pad.querySelectorAll('.keyboard .key.number');
const $clearKey = $pad.querySelector('.keyboard .key.clear');

const PIN_LENGTH = 4;
const PIN = "5678";

$clearKey.addEventListener('click', () => $input.value = '');

$numberKeys.forEach(key => {
    key.addEventListener('click', (e) => {
        if ($input.value.length < PIN_LENGTH) $input.value += e.target.innerHTML;
        if ($input.value.length == 4 && $input.value == PIN) return $input.value = "PASSED";
        if ($input.value.length == 4 && $input.value != PIN) return $input.value = "DENIED"
    })
})
