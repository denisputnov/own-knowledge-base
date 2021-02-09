let $input = document.querySelector('input');

document.querySelectorAll('.key').forEach(key => key.addEventListener('click', (event) => {
    if (event.target.innerHTML == 'Space') return $input.value += ' ';
    $input.value += event.target.innerHTML;
}))