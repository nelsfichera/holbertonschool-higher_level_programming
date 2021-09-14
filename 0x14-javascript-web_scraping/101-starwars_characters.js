#!/usr/bin/node
const request = require('request');
const GET = request.get;
const number = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + number;

const getPromise = charUrl => new Promise((resolve, reject) => {
  GET(charUrl, (err, res, body) => {
    if (err) return (reject(err));
    resolve(JSON.parse(body).name);
  }, 300);
});

const promiseArray = [];

GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  const movies = JSON.parse(body);

  movies.characters.forEach(charUrl => {
    promiseArray.push(getPromise(charUrl));
  });

  Promise.all(promiseArray).then((values) => {
    values.forEach(name => (console.log(name)));
  }).catch(error => console.log(error));
});
