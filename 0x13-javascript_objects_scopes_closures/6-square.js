#!/usr/bin/node
const Square1 = require('./5-square.js');
class Square extends Square1 {
//   constructor (size) {
//     super(size, size);
//   }

  charPrint (c) {
    if (c === 'C' && c !== undefined) {
      const shape = 'C';
      for (let i = 0; i < this.height; i++) {
        console.log(shape.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
