#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv;
const X = 'X';
let sq = '';
const cnv = parseInt(args[2], 10);
if (!isNaN(cnv)) {
  if (cnv > 0) {
    for (let i = 0; i < cnv; i++) {
      for (let j = 0; j < cnv; j++) {
        sq += X;
      }
      sq += '\n';
    }
    console.log(sq.slice(0, -1));
  }
} else {
  console.log('Missing size');
}
