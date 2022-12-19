#!/usr/bin/node
const args = process.argv;

if (args.slice(2).length === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
