#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle () {
  constructor (size) {
    super([arguments]);
  }
}
module.exports = Square;
