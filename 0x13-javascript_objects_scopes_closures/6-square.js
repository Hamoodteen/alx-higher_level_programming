#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

module.exports = class Square extends require('./5-rectangle') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
