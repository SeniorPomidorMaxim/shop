//фиксация навбара
window.addEventListener('scroll', function () {
    document.getElementById('header-nav').classList.toggle('headernav-scroll', window.scrollY > 135);
});
//фиксация навбара


window.addEventListener('DOMContentLoaded', function() {
  // Скрываем все карточки при загрузке страницы
  document.getElementById("liked").style.display = 'none';
  document.getElementById("bought").style.display = 'none';
  document.getElementById("cart").style.display = 'none'; // добавляем строку для скрытия карточки "в корзине"

  // Показываем или скрываем понравившиеся товары при нажатии соответствующей кнопки
  document.getElementById("showLiked").addEventListener("click", function () {
      if(document.getElementById("liked").style.display == 'none') {
          document.getElementById("liked").style.display = 'block';
          document.getElementById("bought").style.display = 'none';
          document.getElementById("cart").style.display = 'none'; // добавленная строка $
      } else {
          document.getElementById("liked").style.display = 'none';
      }
  });

  // Показываем или скрываем купленные товары при нажатии соответствующей кнопки
  document.getElementById("showBought").addEventListener("click", function () {
      if(document.getElementById("bought").style.display == 'none') {
          document.getElementById("liked").style.display = 'none';
          document.getElementById("bought").style.display = 'block';
          document.getElementById("cart").style.display = 'none'; // добавленная строка $
      } else {
          document.getElementById("bought").style.display = 'none';
      }
  });

  // Показываем или скрываем товары в корзине при нажатии соответствующей кнопки
  document.getElementById("showCart").addEventListener("click", function () {
      if(document.getElementById("cart").style.display == 'none') {
          document.getElementById("liked").style.display = 'none';
          document.getElementById("bought").style.display = 'none';
          document.getElementById("cart").style.display = 'block'; // добавленная строка $
      } else {
          document.getElementById("cart").style.display = 'none';
      }
  });
});

// дрочка с иконками выделение цветом
let buttons = document.querySelectorAll('.buttons-container button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        buttons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    });
});
// дрочка с иконками выделение цветом


// карусель похожих товаров
    $(document).ready(function(){
        $(".owl-carousel").owlCarousel({
            items: 4,
            dots: false,  /* Убирает кружочки навигации */
            nav: false,  /* Убирает стрелки навигации */
        });
    });
// карусель похожих товаров