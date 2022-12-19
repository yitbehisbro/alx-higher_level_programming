#!/usr/bin/node
let args = parseInt(process.argv[2]);
if (Number.isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0, string; i < args; i++) {
    string = '';
    for (let j = 0; j < args; j++) {
      string += 'X';
    }
    console.log(string);
  }
}
