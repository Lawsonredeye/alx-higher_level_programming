#!/usr/bin/node
// import the array using require('path/to/file') into a const variable
// log to console the imported list
// create an newList = []
// create
// call the map method on the imported array and inside it we should multiply it by the index
const { list } = require('./100-data.js');
console.log(list);
const newList = list.map((num, index) => num * index);
console.log(newList);
