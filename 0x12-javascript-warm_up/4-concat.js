#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 3) {
  console.log(args[1]+' is '+args[2]);
}
