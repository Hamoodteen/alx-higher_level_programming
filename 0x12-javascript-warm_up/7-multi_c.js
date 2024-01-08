#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv;
const C = 'C is fun';
const cnv = parseInt(args[2], 10);
if (!isNaN(args[2])) {
  if (args[2] > 0) {
    for (let index = 0; index < args[2]; index++) {
      console.log(C);
    }
  }
} else {
  console.log('Missing number of occurrences');
}
