#!/usr/bin/node
const args = process.argv.slice(2);

if (args[2]) {
  if (isNaN(parseInt(args[2], 10))) {
    console.log('Not a number');
  } else {
    console.log('My number: '+args[2]);
} else {
  console.log('Not a number');
}
