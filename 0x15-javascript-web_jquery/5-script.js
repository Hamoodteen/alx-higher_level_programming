#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

$('div#add_item').on('click', function () {
  const ls = $('ul.my_list');
  ls.append('<li>Item</li>');
});
