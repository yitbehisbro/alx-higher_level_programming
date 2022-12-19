#!/usr/bin/node
const args = process.argv;
let string;

if (isNaN(parseInt(args[1]))) {
  string = 'Missing number of occurrences';
  console.log(string);
} else {
  string = 'C is fun';
  for (let i = 0; i <= args[1]; i++) {
    console.log(string);
  }
}
