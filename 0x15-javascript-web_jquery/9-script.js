const $ = window.$;
const fetch = window.fetch;
async function hello (url) {
  const response = await fetch(url);
  const dict = await response.json();
  $('DIV#hello').append(dict.hello);
}
hello('https://fourtonfish.com/hellosalut/?lang=fr');
