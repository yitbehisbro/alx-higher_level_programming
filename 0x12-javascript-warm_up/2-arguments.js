#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length > 1)
{
	console.log('Arguments found');
}
else if (argv.length == 1)
{
	console.log('Argument found');
}
else
{
	console.log('No argument');
}
