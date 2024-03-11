#!/usr/bin/node
/**
 * create a let variable named process and assign the value = require('process')
 * using a conditional, check, if the process.argv[2] === undefined then print no argument else print process.argv[2] member
 */

const process = require('process');
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
