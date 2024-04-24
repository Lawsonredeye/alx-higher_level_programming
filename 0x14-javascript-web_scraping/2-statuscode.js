#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

request(arg, { method: 'GET' }, (err, response) => {
  if (err) {
    console.error(err);
  }
  console.log('code:', response.statusCode);
});
