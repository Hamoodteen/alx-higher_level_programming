#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

$(document).ready(function () {
  const charapi = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  fetch(charapi)
    .then(response => {
      return response.json();
    })
    .then(data => {
      const char = $('div#character');
      char.append(data.name);
    });
});
