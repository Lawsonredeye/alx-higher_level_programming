#!/usr/bin/node
const process = require('process');
if (Number(process.argv[2]) === Number(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
