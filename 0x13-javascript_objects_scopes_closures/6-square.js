#!/usr/bin/node
const SquareParent = require('./5-square');
const Rectangle = require('./4-rectangle');

class Square extends SquareParent {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let string = '';
        for (let j = 0; j < this.width; j++) {
          string += c;
        }
        console.log(string);
      }
    } else {
      Rectangle.print ();
    }
  }
}
module.exports = Square;
