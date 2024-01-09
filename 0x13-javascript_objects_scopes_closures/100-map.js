#!/usr/bin/node

// commenttttttttttttttttttttttttttttt

exports.data = require('./100-data.js').list;
console.log(this.data);
const newlist = this.data.map((x) => x * this.data.indexOf(x));
console.log(newlist);
