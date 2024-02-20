#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const myurl = 'https://swapi-api.alx-tools.com/api/films/';
req({ url: myurl, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let cnt = 0;
    const films = JSON.parse(body);
    for (const i of films.results) {
      for (const j of i.characters) {
        if (j === 'https://swapi-api.alx-tools.com/api/people/18/') {
          cnt++;
        }
      }
    }
    console.log(cnt);
  }
});
