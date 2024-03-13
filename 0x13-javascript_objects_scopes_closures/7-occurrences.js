#!/usr/bin/node
// create a let var count = 0
// loop through the list.length
// check if the element is found while searching, if its found incre,ent count += 1
// return the count

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
