#!/usr/bin/node
const request = require('request');
const GET = request.get;
const fs = require('fs');
const write = fs.writeFile;
const url = process.argv[2];
const filename = process.argv[3];

GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  write(filename, body, 'utf8', (err) => {
    if (err) return (console.log(err));
  });
});
