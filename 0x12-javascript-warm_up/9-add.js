#!/usr/bin/node
function add(a, b) { return a + b }
const args = process.argv;
if (args.slice(2).length < 3) {
  console.log('NaN');
} else {
  if (isNaN(parseInt(args[1])) && isNaN(parseInt(args[2]))) {
    console.log('NaN');
  }
  console.log(add(parseInt(args[1]), parseInt(args[2])));
}
