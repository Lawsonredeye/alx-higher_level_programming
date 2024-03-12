#!/usr/bin/node
/**
 * create a const var process to store the args list
 * create a function that adds 2 argument variable together and print the output
 * using the add function, add both process.argv[2] + process.argv[3]
 */
const process = require('process');
function add (a, b) {
  a = Number(a);
  b = Number(b);
  console.log(a + b);
}
add(process.argv[2], process.argv[3]);
