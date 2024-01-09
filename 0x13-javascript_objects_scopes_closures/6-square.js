#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// commenttttttttttttttttttttttttttttt

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const CX = c === undefined ? 'X' : 'C';
    let sq = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        sq += CX;
      }
      sq += '\n';
    }
    console.log(sq.slice(0, -1));
  }
};
