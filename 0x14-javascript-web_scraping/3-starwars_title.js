#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const args = process.argv;
const myurl = ('https://swapi-api.alx-tools.com/api/films/' + args[2]);
req({ url: myurl, methods: 'GET' }, function (err, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
