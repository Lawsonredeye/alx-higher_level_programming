#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${arg}`, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});