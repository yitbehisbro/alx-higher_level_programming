#!/usr/bin/node
const args = parseInt(process.argv);

if (isNaN(args[1])) {
  string = 'Missing number of occurrences';
  console.log(string);
} else {
  string = 'C is fun';
  for (let i = 0; i <= args[1]; i++) {
    console.log(string);
  }
}
