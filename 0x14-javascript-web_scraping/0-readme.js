#!/usr/bin/node

/**
 * script that reads and prints the content of a file.
 * import fs with the require keyword to a variable called fs
 * create a variable to store the command line arg
 * using the fs.readFile() with asynchrous callback to catch errors
 * print out the value
 */

const fs = require('fs');
const args = process.argv[2];

fs.readFile(args, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
