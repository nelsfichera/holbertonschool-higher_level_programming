#!/usr/bin/node
const fs = require('fs');
const av = process.argv;
const dataA = fs.readFileSync(av[2], 'UTF-8');
const dataB = fs.readFileSync(av[3], 'UTF-8');
fs.writeFileSync(av[4], (dataA + dataB), 'UTF-8');
