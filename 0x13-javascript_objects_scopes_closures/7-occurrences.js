#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      sum += 1;
    }
  }
  return sum;
};
