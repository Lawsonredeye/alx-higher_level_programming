#!/usr/bin/node

/**
 * script that writes a string to a file.
 * import fs and process using argv
 * store the 2 & 3 args into 2 var
 * using fs.writeFile place the path and the data
 * using the callback func print any err that was encountered
 */

const fs = require('fs');
const arg2 = process.argv[2];
const arg3 = process.argv[3];

fs.writeFile(arg2, arg3, { option: 'utf-8' }, (err, data) => {
  if (err) {
    console.err(err);
  }
});
