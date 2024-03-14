#!/usr/bin/node

const { dict } = require('./101-data.js');
const newdict = {};
let key = 0;
for (key in dict) {
  if (Object.prototype.hasOwnProperty.call(newdict, dict[key])) {
    newdict[dict[key]].push(key);
  } else {
    const newArray = [];
    newArray.push(key);
    newdict[dict[key]] = newArray;
  }
}
console.log(newdict);
