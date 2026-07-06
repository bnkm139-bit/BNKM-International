/* BNKM International — shared site behaviour */
document.addEventListener('DOMContentLoaded', function () {

  /* Mobile nav toggle */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      var expanded = nav.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { nav.classList.remove('open'); });
    });
  }

  /* Sticky header shadow on scroll */
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 8) header.style.boxShadow = '0 4px 18px rgba(6,27,49,0.25)';
      else header.style.boxShadow = 'none';
    });
  }

  /* Generic form submit handler: prevent default, show success message */
  document.querySelectorAll('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var requiredOk = true;
      form.querySelectorAll('[required]').forEach(function (field) {
        if (!field.value || (field.type === 'checkbox' && !field.checked)) requiredOk = false;
      });
      if (!requiredOk) {
        form.reportValidity();
        return;
      }
      var successEl = form.parentElement.querySelector('.form-success') || form.querySelector('.form-success');
      if (successEl) {
        successEl.classList.add('show');
        successEl.setAttribute('tabindex', '-1');
        successEl.focus();
      }
      form.reset();
      document.querySelectorAll('.file-input span').forEach(function (span) {
        span.textContent = span.getAttribute('data-default') || span.textContent;
      });
    });
  });

  /* File input label update */
  document.querySelectorAll('.file-input input[type="file"]').forEach(function (input) {
    var span = input.closest('.file-input').querySelector('span');
    if (span && !span.getAttribute('data-default')) span.setAttribute('data-default', span.textContent);
    input.addEventListener('change', function () {
      if (input.files && input.files.length) {
        span.textContent = input.files[0].name;
      }
    });
  });

  /* Current year in footer */
  var yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});
