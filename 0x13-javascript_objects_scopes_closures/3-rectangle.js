#!/usr/bin/node
class Rectangle {
  width;
  height;

  constructor(w, h) {
    this.width = w;
    this.height = h;
    if (w === 0 || h === 0) {
      new Rectangle();
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string += 'X';
      }
      console.log(string);
    }
  }
}
module.exports = Rectangle;
