#!/usr/bin/node
const args = process.argv;
let num = parseInt(args[1]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i <= num; i++) {
    console.log('C is fun');
}
