#!/usr/bin/node
// create a reverseList = []
// access the last element of the list using list.lenght - 1 to the loop counter and decrement the value into a new list and return the reverseList
exports.esrever = function (list) {
  const reverseList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return reverseList;
};
