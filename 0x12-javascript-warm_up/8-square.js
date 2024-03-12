#!/usr/bin/node
/**
 * print a square
 * create a const var named process that stores the value require
 * check if the first argument is a number, if it isnt then print missing size.
 * else create a loop to iterate through the size of the square and use the .repeat() method to print the string 'x' * size.
 */
const process = require('process');
const x = 'x';
if (Number(process.argv[2])) {
  const newNum = Number(process.argv[2]);
  for (let i = 0; i < newNum; i++) {
    console.log(x.repeat(newNum));
  }
} else {
  console.log('Missing size');
}
