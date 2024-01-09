#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// commenttttttttttttttttttttttttttttt

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const CX = String(c);
      let sq = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          sq += CX;
        }
        sq += '\n';
      }
      console.log(sq.slice(0, -1));
    }
  }
};
