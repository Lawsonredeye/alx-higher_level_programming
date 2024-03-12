#!/usr/bin/node
// create a class named rectangle
// add a constructor with the parameter w & h
// check if w and h are greater than 0 then
// instatiate this.width and this.height = w & h respectively
// create a method print() with no param that prints the w * h of a rectangle
// inside the method using a loop
// create a const shape = 'X'
// using a loop with the length of the loop as height
// repeat the string by the size of the width and log the shape var.
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const shape = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(shape.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
