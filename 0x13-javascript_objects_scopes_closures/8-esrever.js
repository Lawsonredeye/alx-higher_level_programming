#!/usr/bin/node
// create a emptyList = []
// access the last element of the list using list.lenght - 1 to the loop counter and decrement the value into a new list and return the emptyList
exports.esrever = function (list) {
  const emptyList = [];
  for (let i = list.length - 1; i > 0; i--) {
    emptyList.push(list[i]);
  }
  return emptyList;
};
