#!/usr/bin/node
function add (a, b) {
  const c = parseInt(a) + parseInt(b);
  console.log(c);
  return c;
}
add(process.argv[2], process.argv[3]);
