#!/usr/bin/node
const request = require('request');
const GET = request.get;
const number = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + number;

GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  const movies = JSON.parse(body);

  movies.characters.forEach(charUrl => GET(charUrl, (err, res, body) => {
    if (err) return (console.log(err));
    console.log(JSON.parse(body).name);
  }));
});
