#!/usr/bin/node
/**
 * create a const var named process and assign the value require ('process')
 * using console.log, concat process.argv[2] + process.argv[3]
 */

const process = require('process');
console.log(process.argv[2] + ' is ' + process.argv[3]);
