#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.sort(function (a, b) { return b - a});
  console.log(process.argv[3]);
}
