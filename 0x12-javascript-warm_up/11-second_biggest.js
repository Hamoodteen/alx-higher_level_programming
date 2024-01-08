#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const args = process.argv.slice(2);
const nums = args.map(Number);
const mdnums = nums.filter(item => item !== Math.max(...args));
console.log(Math.max(...mdnums));
