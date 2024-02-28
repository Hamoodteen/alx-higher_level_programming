#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

$('div#toggle_header').on('click', function () {
  const header = $('header');
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  }
});
