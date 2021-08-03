#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
