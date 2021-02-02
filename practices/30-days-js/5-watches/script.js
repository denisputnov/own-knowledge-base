window.onload = () => {
    const $watch = document.querySelector('.watches');
    setInterval(updateWatch, 500);   
    
    function updateWatch() {
        let time = new Date();
    
        $watch.querySelector('.watches__hours').innerHTML = time.getHours(); 
        $watch.querySelector('.watches__minutes').innerHTML = time.getMinutes();
        $watch.querySelector('.watches__seconds').innerHTML = time.getSeconds();
    }
}