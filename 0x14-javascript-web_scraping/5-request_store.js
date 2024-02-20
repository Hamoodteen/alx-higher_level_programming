#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const fs = require('fs');
const args = process.argv;
req(args[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(args[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
