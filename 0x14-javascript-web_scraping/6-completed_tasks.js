#!/usr/bin/node
// commenttttttttttttttttttttttttttttt

const req = require('request');
const args = process.argv;
const myurl = (args[2]);
req({ url: myurl, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonbody = JSON.parse(body);
    let done = 0;
    const donelist = [];
    const donedict = {};
    for (let i = 1; i < 11; i++) {
      for (let j = (i - 1) * 20; j < ((i - 1) * 20) + 20; j++) {
        if (jsonbody[j].completed) {
          done++;
        }
      }
      donelist.push(done);
      done = 0;
    }
    donelist.forEach((value, index) => {
      donedict[index + 1] = value;
    });
    console.log(donedict);
  }
});
