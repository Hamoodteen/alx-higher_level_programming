#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const data = require('./101-data').dict;
const keys = Object.keys(data);
for (const key of keys) {
  data.reduce((count, value) => (value === key ? count + 1 : count), 0);
}
