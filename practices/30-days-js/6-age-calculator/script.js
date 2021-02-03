let $calculator = document.querySelector('.calculator');
let $resultHeader = $calculator.querySelector('.calculator__result');
let $date = $calculator.querySelector('#date');
let $button = $calculator.querySelector('.calculator__button');

$button.addEventListener('click', () => {
    let _dateString = $date.value.toString();
    
    let _date = new Date(
        parseInt(_dateString.substring(0,4), 10),
        parseInt(_dateString.substring(5, 8), 10) - 1,
        parseInt(_dateString.substring(8, 11), 10),
    ).getTime();
    
    let _now = new Date().getTime();

    let _difference = _now - _date;

    if (_difference < 0) {
        $resultHeader.innerHTML = "You can't choose date from the future :)"
        return;
    }

    let year_age = Math.floor(_difference / 31536000000);
    let day_age = Math.floor((_difference % 31536000000) / 86400000);
    let month_age = Math.floor(day_age / 30);
    
    day_age = day_age % 30;

    return $resultHeader.innerHTML = `${year_age} years, ${month_age} months, ${day_age} days`
})
