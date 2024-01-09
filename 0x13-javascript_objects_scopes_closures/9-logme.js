#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

let cnt = 0;
exports.logMe = function (item) {
  console.log(cnt + ': ' + item);
  cnt++;
};
