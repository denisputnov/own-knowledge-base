$(function() {
    $('.calculator .calculator__button').click(function() {
        let _dateString = $('.calculator #date').val().toString();
        console.log($('.calculator #date'));
    
        let _date = new Date(
            parseInt(_dateString.substring(0,4), 10),
            parseInt(_dateString.substring(5, 8), 10) - 1,
            parseInt(_dateString.substring(8, 11), 10),
        ).getTime();
        
        let _now = new Date().getTime();
        
        let $resultHeader = $('.calculator .calculator__result');
        
        let _difference = _now - _date;
        
        if (_difference < 0) {
            $resultHeader.html("You can't choose date from the future :)");
            return;
        }
    
        let year_age = Math.floor(_difference / 31536000000);
        let day_age = Math.floor((_difference % 31536000000) / 86400000);
        let month_age = Math.floor(day_age / 30);
        
        day_age = day_age % 30;

        return $resultHeader.html(`${year_age} years, ${month_age} months, ${day_age} days`);
    });
});