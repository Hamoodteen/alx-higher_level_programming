#!/usr/bin/node

// commenttttttttttttttttttttttttttttt

const data = require('./100-data.js');
console.log(data.list);
const newlist = data.list.map((x) => x * data.list.indexOf(x));
console.log(newlist);
