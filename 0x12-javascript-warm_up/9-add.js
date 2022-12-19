#!/usr/bin/node
function add(a, b) { return a + b }
const args = process.argv;
if (args.slice(2).length < 3) {
  console.log('NaN');
} else {
  console.log(add(parseInt(args[1]), parseInt(args[2])));
}
