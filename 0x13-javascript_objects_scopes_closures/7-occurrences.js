#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, value) => (value === searchElement ? count + 1 : count), 0);
};
