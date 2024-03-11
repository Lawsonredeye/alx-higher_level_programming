#!/usr/bin/node
const process = require('process');
if (Number(process.argv[2])) {
  const newNum = Number(process.argv[2]);
  for (let i = 0; i < newNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
