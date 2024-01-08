#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv;
const C = 'C is fun';
const cnv = parseInt(args[2], 10);
if (!isNaN(cnv)) {
  if (cnv > 0) {
    for (let index = 0; index < cnv; index++) {
      console.log(C);
    }
  }
} else {
  console.log('Missing number of occurrences');
}
