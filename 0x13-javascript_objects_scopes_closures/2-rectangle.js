#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) || (h > 0)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = {};
      this.height = {};
    }
  }
};
