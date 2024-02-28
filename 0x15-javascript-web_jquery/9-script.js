#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

$(document).ready(function () {
  const hello = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  fetch(hello)
    .then(response => {
      return response.json();
    })
    .then(data => {
      const hi = $('div#hello');
      hi.append(data.hello);
    });
});
