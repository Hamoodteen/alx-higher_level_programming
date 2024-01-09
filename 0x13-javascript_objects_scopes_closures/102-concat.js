#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const fs = require('fs');
const args = process.argv;
const first = fs.readFileSync(args[2], 'utf8');
const second = fs.readFileSync(args[3], 'utf8');
fs.writeFileSync(args[4], first + second);
