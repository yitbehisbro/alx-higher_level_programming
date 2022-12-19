#!/usr/bin/node
const args = parseInt(process.argv);
let string;
if (isNaN(args[0])) {
  string = 'Missing number of occurrences';
  console.log(string);
} else {
  string = 'C is fun';
  console.log(string);
  for (let i = 0; i <= args[0]; i++) {
    console.log(string);
  }
}
