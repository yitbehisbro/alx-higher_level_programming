#!/usr/bin/node
const args = process.argv;
if (args.slice(2).length > 1)
{
	console.log('Arguments found');
}
else if (args.slice(2).length === 1)
{
	console.log('Argument found');
}
else
{
	console.log('No argument');
}
