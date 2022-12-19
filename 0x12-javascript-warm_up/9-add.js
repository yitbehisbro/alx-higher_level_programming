#!/usr/bin/node
function add(a, b) {
  return a + b;
}
const args = process.argv.slice(2);
if (args.length < 3) {
  console.log('NaN');
} else {
  console.log(add(parseInt(args[1]), parseInt(args[2])));
}
