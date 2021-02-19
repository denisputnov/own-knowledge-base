let element = document.getElementById('osm-map');
element.style = 'height:600px;';

let map = L.map(element);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let target = L.latLng('55.751244', '37.618423');

map.setView(target, 14);
L.marker(target).addTo(map);