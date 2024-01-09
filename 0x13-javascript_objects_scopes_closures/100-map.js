#!/usr/bin/node

// commenttttttttttttttttttttttttttttt

exports.data = require('./100-data.js').list;
console.log(exports.data);
const newlist = exports.data.map((x) => x * exports.data.indexOf(x));
console.log(newlist);
