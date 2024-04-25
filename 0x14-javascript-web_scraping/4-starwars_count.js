#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];

// use request to GET data from the API
request(arg, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  // Store the parsed JSON data into an object
  const obj = JSON.parse(body).results;
  let count = 0;

  // Using a forEach method, loop through the list to get all matching index
  obj.forEach(objx => {
    if (objx.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });
  console.log(count);
});
