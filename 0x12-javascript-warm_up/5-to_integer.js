#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv;
const cnv = parseInt(args[2], 10);
console.log(isNaN(cnv) ? 'My number: ' + cnv : 'Not a number');
