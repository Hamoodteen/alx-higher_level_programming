#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv;
if (args.length > 2) {
	console.log(process.argv.length === 3 ? 'Argument found' : 'Arguments found');
} else {
	console.log('No argument');
}
