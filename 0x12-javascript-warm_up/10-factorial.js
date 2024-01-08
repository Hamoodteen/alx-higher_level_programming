#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

function factorial (a) {
  if (isNaN(a) || a === 0 || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

const args = process.argv;
const n = parseInt(args[2]);
console.log(factorial(n));
