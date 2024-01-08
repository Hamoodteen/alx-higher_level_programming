#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

import { argv } from 'process';
if (process.argv.length() > 1) {
	console.log(process.argv.length() === 2 ? 'Argument found' : 'Arguments found');
}
else {
	console.log('No argument');
}
