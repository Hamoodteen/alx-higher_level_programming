#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

$(document).ready(function () {
  const titleapi = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  fetch(titleapi)
    .then(response => {
      return response.json();
    })
    .then(data => {
      const char = $('ul#list_movies');
      data.results.forEach(title => {
        char.append('<li>' + title.title + '</li>');
      });
    });
});
