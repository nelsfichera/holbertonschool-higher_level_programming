#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let x = list.length; x >= 0; x--) {
    reversed.push(list[x]);
  }
  reversed.shift();
  return reversed;
};
