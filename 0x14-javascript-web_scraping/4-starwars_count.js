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
    for (let i = 0; i < films.results.length; i++) {
      const characters = films.results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
          cnt++;
        }
      }
    }
    console.log(cnt);
  }
});
