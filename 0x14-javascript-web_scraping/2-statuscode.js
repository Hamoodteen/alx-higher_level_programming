#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const args = process.argv;
req(args[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
