#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
