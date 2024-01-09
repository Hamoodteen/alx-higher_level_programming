#!/usr/bin/node

// commenttttttttttttttttttttttttttttt

const data = require('./100-data.js').list;
console.log(data);
const newlist = data.map((x) => x * data.indexOf(x));
console.log(newlist);
