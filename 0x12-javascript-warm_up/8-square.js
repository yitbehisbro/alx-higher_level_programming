#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0, s; i < num; i++) {
    s = '';
    for (let j = 0; j < num; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
