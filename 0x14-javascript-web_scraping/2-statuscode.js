#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const args = process.argv;
req(args[2], function (response) {
  console.log('code: ' + response.statusCode);
});
