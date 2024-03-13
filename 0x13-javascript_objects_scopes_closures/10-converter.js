#!/usr/bin/node
// value = 5;
// console.log(toString(10));
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
