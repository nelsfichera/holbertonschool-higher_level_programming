#!/usr/bin/node
const request = require('request');
const GET = request.get;
const number = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + number;

GET(url, (err, response, body) => {
  if (err) return (console.log(err));
  console.log(JSON.parse(body).title);
});
