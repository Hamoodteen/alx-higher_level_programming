#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

$(document).ready(function () {
  const lang = $('input#language_code').val();
  const hello = 'https://hellosalut.stefanbohacek.dev/?lang='.concat(lang);
  fetch(hello)
    .then(response => {
      return response.json();
    })
    .then(data => {
      $('input#btn_translate').on('click', function () {
        $('div#hello').text(data.hello);
        console.log(hello);
      });
    });
});
