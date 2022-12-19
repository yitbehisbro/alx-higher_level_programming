#!/usr/bin/node
const args = process.argv.slice(2);

if (isNaN(parseInt(args[1], 10))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[1]; i++) {
    console.log('C is fun');
  }
}
