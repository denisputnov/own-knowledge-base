const $select = document.querySelector('.tracker #select');
const $input = document.querySelector('.tracker input');

let coins;

fetch("https://api.coinstats.app/public/v1/coins?skip=0&limit=100&currency=USD", {
    // mode: "no-cors"
})
.then(resp => resp.json())
.then(data => {
    coins = data.coins;
    coins.forEach(coin => {
        $select.insertAdjacentHTML("beforeend", `<option value="${coin.price}">${coin.name}</option>`);
    });
    $input.value = coins[0].price;
});

document.querySelector('#select').addEventListener('change', () => $input.value = document.querySelector('#select').value)