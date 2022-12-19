#!/usr/bin/node
let args = parseInt(process.argv[2]);
if (Number.isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0, s; i < args; i++) {
    s = '';
    for (let j = 0; j < args; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
