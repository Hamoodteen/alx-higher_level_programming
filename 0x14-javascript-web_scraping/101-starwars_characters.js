#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const args = process.argv;
const myurl = ('https://swapi-api.alx-tools.com/api/films/' + args[2]);
req({ url: myurl, methods: 'GET' }, function (err1, response2, body1) {
  if (err1) {
    console.log(err1);
  } else {
    for (let i = 0; i < JSON.parse(body1).characters.length; i++) {
      req({ url: JSON.parse(body1).characters[i], methods: 'GET' }, function (err2, response2, body2) {
        if (err2) {
          console.log(err2);
        } else {
          console.log(JSON.parse(body2).name);
        }
      });
    }
  }
});
