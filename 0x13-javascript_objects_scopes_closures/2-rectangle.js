#!/usr/bin/node
// create a class named rectangle
// add a constructor with the parameter w & h
// check if w and h are greater than 0 then
// instatiate this.width and this.height = w & h respectively
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
