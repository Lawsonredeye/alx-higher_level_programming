#!/usr/bin/node
// use a closure function, return the new function
// innerfunc should have a count variable
// if new argument is passed increment count
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
//   return function newLog(item) {
//   };
};
