function _getRandomNumber(min, max) {
    // get random number from (min-0.5) to (max+0.5)
    let rand = min - 0.5 + Math.random() * (max - min + 1);
    return Math.round(rand);
}

window.onload = () => {
    const $generator = document.querySelector('.generator');
    const $button = $generator.querySelector('.generator__button');

    $button.addEventListener('click', () => {
        // get random number
        let randNum = _getRandomNumber(
            $generator.querySelector('#min_generator_value').value,
            $generator.querySelector('#max_generator_value').value
        );
        
        // insert random number into header 
        $generator.querySelector('.generator__result').innerHTML = `Result is: ${randNum}`;
    }); 
};