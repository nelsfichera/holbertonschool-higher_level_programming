const $ = window.$;
const fetch = window.fetch;
async function characterName (url) {
  const response = await fetch(url);
  const dict = await response.json();
  $('DIV#character').text(dict.name);
}
characterName('https://swapi-api.hbtn.io/api/people/5/?format=json');
