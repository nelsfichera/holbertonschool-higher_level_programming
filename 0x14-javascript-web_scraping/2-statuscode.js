#!/usr/bin/node
const request = require('request');
const GET = request.get;
const url = process.argv[2];

GET(url, (err, response, body) => {
  if (err) return (console.log(err));
  console.log('code: ' + response.statusCode);
});
