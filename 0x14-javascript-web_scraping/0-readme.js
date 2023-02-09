#!/usr/bin/node

const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[1], 'utf8', function (err, data) {
	console.log(data);
	if (err) console.log('Error: ', err);
});
