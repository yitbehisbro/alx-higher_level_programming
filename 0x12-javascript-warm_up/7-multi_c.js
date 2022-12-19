#!/usr/bin/node
const args = parseInt(process.argv);
let string;

if (isNaN(args[1])) {
  string = 'Missing number of occurrences';
  console.log(string);
} else {
  string = 'C is fun';
  for (let i = 0; i <= args[1]; i++) {
    console.log(string);
  }
}
