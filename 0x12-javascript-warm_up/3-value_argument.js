#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv;
if (args.length > 2) {
  console.log(process.argv[3]);
} else {
  console.log('No argument');
}
