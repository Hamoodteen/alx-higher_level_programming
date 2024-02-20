#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const args = process.argv;
req(('https://swapi-api.alx-tools.com/api/films/' + args[2]), function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body.title);
  }
});
