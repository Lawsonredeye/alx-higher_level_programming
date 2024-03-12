#!/usr/bin/node
/**
 * create a const var to store the args list
 * check if both the argv[2] and argv[3] are both numbers if they are, then add them together and print the output
 */
const process = require('process');
function add (a, b) {
  a = Number(a);
  b = Number(b);
  console.log(a + b);
}
add(process.argv[2], process.argv[3]);
