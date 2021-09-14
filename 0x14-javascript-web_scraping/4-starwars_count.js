#!/usr/bin/node
const request = require('request');
const GET = request.get;
const url = process.argv[2];

GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  const movies = JSON.parse(body).results;
  let count = 0;

  for (let x = 0; x < movies.length; x++) {
    for (let n = 0; n < movies[x].characters.length; n++) {
      if (movies[x].characters[n].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
