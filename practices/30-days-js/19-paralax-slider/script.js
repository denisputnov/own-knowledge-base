const slider = document.querySelector('.swiper-container');

let mySwiper = new Swiper(slider, {
    slidesPerView: 1,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    loop: true,
    parallax: true,
    autoplay: {
        delay: 5000,
    }
});