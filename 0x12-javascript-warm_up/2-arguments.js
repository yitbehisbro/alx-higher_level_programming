#!/usr/bin/node
const process = require('process');
var args = process.argv;
if (args.length > 1)
{
	console.log('Arguments found');
}
else if (args.length === 1)
{
	console.log('Argument found');
}
else
{
	console.log('No argument');
}
