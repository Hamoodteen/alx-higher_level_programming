#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv;
const X = 'X';
const cnv = parseInt(args[2], 10);
if (!isNaN(cnv)) {
  if (cnv > 0) {
    for (let i = 0; i < cnv; i++) {
      for (let j = 0; j < cnv; j++) {
        console.log(X);
      }
    }
  }
} else {
  console.log('Missing number of occurrences');
}
