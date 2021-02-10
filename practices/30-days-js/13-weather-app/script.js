const $app = document.getElementById('app');
const API_KEY = 'cd4894fa6fe57413646a3d6d029c3967'; // just for example

const $input = $app.querySelector('input');
let $res = document.getElementById('res');

$app.querySelector('button').addEventListener('click', async () => {
    let _city = $input.value.trim();
    $input.value = '';
    console.log(await fetch(`http://api.openweathermap.org/data/2.5/weather?q=${_city}&APPID=${API_KEY}&units=metric`)
        .then(function(resp) { 
            return resp.json() 
        }) // Convert data to json
        .then(function(data) {
            console.log(data);
            if (data.message == 'city not found') return $res.innerHTML = "Invalid City";
            return $res.innerHTML = `
            ${data.weather[0].description}</br>
            temp is: ${data.main.temp}</br>
            feels like: ${data.main.feels_like}`
        })
        .catch(function() {
            console.log('error');
        })
    );
});
