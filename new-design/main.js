const mobileToggle = document.querySelector('[data-mobile-toggle]');
const mobileMenu = document.querySelector('[data-mobile-menu]');
const accordions = document.querySelectorAll('[data-accordion]');
const dropdownButtons = document.querySelectorAll('.has-dropdown > button');

if (mobileToggle && mobileMenu) {
  mobileToggle.addEventListener('click', () => {
    const expanded = mobileToggle.getAttribute('aria-expanded') === 'true';
    mobileToggle.setAttribute('aria-expanded', String(!expanded));
    mobileMenu.classList.toggle('open');
  });
}

accordions.forEach((btn) => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!expanded));
    const submenu = btn.nextElementSibling;
    if (submenu) submenu.classList.toggle('open');
  });
});

dropdownButtons.forEach((btn) => {
  const parent = btn.closest('.has-dropdown');
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    const open = parent?.classList.contains('open');
    document.querySelectorAll('.has-dropdown.open').forEach((item) => item.classList.remove('open'));
    if (!open) parent?.classList.add('open');
  });
});

document.addEventListener('click', (e) => {
  if (!(e.target instanceof Element)) return;
  if (!e.target.closest('.has-dropdown')) {
    document.querySelectorAll('.has-dropdown.open').forEach((item) => item.classList.remove('open'));
  }
});
