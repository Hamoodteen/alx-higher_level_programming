#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv.slice(2);
const nums = args.map(Number);
const mdnums = nums.filter(item => item !== Math.max(...args));
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  console.log(Math.max(...mdnums));
}
