/* Znews Studio: nhớ giao diện sáng/tối dùng chung với trang chủ và cẩm nang. */
(function () {
  var KEY = 'znews_theme';
  var root = document.documentElement;

  function read() {
    try { return localStorage.getItem(KEY) || 'light'; } catch (e) { return 'light'; }
  }
  function save(v) {
    try { localStorage.setItem(KEY, v); } catch (e) { /* trình duyệt chặn lưu trữ */ }
  }

  root.setAttribute('data-theme', read());

  document.addEventListener('click', function (ev) {
    var t = ev.target.closest ? ev.target.closest('[data-theme-toggle]') : null;
    if (!t) return;
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    save(next);
  });
})();
