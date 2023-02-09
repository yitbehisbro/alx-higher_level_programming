#!/usr/bin/node
const fs = require('fs');
const process = require('process');

try {
  const content = fs.readFileSync(process.argv[2], 'utf8');
  console.log(content);
} catch (err) {
  console.error('Error: ' + err.message);
}
