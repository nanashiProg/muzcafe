let lastScrollTop = 0;
const header = document.querySelector('.header'); // или по вашему классу/id
const sidebar_menu = document.querySelector('.sidebar_menu'); // или по вашему классу/id

window.addEventListener('scroll', () => {
  let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

  // Проверка: прокрутили ли мы страницу ниже высоты самой шапки (чтобы она не прыгала в самом верху)
  if (currentScroll > 60) {
    if (currentScroll > lastScrollTop) {
      // Скролл вниз — скрываем шапку
      header.classList.add('header--hidden');
      if (sidebar_menu) sidebar_menu.classList.add('sidebar--hidden');
    } else {
      // Скролл вверх — показываем шапку
      header.classList.remove('header--hidden');
      if (sidebar_menu) sidebar_menu.classList.remove('sidebar--hidden');
    }
  } else {
    // В самом верху страницы шапка всегда видна
    header.classList.remove('header--hidden');
    if (sidebar_menu) sidebar_menu.classList.remove('sidebar--hidden');
  }

  // Обновляем значение для следующей проверки.
  // Math.max предотвращает отрицательные значения скролла на iOS (эффект bounce)
  lastScrollTop = Math.max(0, currentScroll);
});