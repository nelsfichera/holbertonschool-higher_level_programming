#!/usr/bin/node
const fs = require('fs');
const write = fs.writeFile;
const filename = process.argv[2];
const data = process.argv[3];

write(filename, data, 'utf8', (err) => {
  if (err) return (console.log(err));
});
