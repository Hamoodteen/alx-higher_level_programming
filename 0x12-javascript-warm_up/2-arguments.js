#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

import { argv } from 'process';
if (process.argv != 0) {
	console.log(process.argv.length() == 1 ? 'Argument found' : 'Arguments found');
}
else {
	console.log('No argument');
}
