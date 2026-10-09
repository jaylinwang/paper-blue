const buttons = [...document.querySelectorAll('[data-mode]')];
const size = document.querySelector('#size');
const width = document.querySelector('#width');
function mode(value) {
  document.body.classList.toggle('theme-dark', value === 'dark');
  document.body.classList.toggle('theme-light', value === 'light');
  document.documentElement.style.colorScheme = value;
  buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.mode === value)));
}
function update() {
  document.body.style.setProperty('--font-text-size', `${size.value}px`);
  document.body.style.setProperty('--file-line-width', `${width.value}px`);
  document.querySelector('#size-value').value = `${size.value} px`;
  document.querySelector('#width-value').value = `${width.value} px`;
}
buttons.forEach(button => button.addEventListener('click', () => mode(button.dataset.mode)));
size.addEventListener('input', update);
width.addEventListener('input', update);
document.querySelector('#reset').addEventListener('click', () => { size.value = 17; width.value = 720; mode('light'); update(); });
document.querySelectorAll('.task-list-item input').forEach(input => input.addEventListener('change', () => input.closest('li').classList.toggle('is-checked', input.checked)));
