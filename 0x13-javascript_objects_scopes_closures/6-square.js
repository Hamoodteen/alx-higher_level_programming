#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

module.exports = class Square extends require('./5-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const CX = (c === undefined ? 'X' : String(c));
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
