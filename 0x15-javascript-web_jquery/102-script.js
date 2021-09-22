const $ = window.$;
const fetch = window.fetch;
document.onreadystatechange = function () {
  if (document.readyState === 'complete') {
    async function hello (url) {
      const response = await fetch(url);
      const dict = await response.json();
      $('DIV#hello').append(dict.hello);
    }
    $('INPUT#btn_translate').click(function () {
      const lang = $('INPUT#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
      hello(url);
    });
  }
};
