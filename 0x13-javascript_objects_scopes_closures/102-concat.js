#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const fs = require('fs');
const args = process.argv;
let first = '';
let second = '';
fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) throw err;
  first = data;
});
fs.readFile(args[3], 'utf8', (err, data) => {
  if (err) throw err;
  second = data;
});
fs.writeFile(args[4], first + second, 'utf8', (err) => {
  if (err) throw err;
});
