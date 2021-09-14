#!/usr/bin/node

const fs = require('fs');
const rf = fs.readFile;
const argv = process.argv;

rf(argv[2], 'utf8', (err, data) => {
  if (err) return (console.log(err));
  console.log(data);
});
