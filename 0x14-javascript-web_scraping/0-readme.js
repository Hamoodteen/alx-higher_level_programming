#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const fs = require('fs');
const args = process.argv;
const fileName = args[2];
fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
