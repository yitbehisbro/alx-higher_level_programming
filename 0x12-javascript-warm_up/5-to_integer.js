#!/usr/bin/node
const args = process.argv;
let num;
num = parseInt(args[2]);
if (isNaN(num)) {
  num = 'Not a number';
} else {
  num = ('My number: ' + num);
}
console.log(num);
