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
}
module.exports = Rectangle;
