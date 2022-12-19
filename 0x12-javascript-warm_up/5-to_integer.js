#!/usr/bin/node
const args = process.argv;

if (args[1]) {
  if (isNaN(parseInt(args[1], 10))) {
    console.log('Not a number');
  } else {
    console.log('My number: '+args[1]);
} else {
  console.log('Not a number');
}
