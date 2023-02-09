#!/usr/bin/node
const fs = require('fs');
const process = require('process');

try {
  fs.writeFileSync(process.argv[2], process.argv[3], 'utf8');
} catch (err) {
  console.error('Error: ' + err.message);
}
