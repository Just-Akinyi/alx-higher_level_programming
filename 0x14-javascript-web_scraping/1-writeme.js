#!/usr/bin/node
const fs = require('fs');
const myfile = process.argv[2];
fs.readFile(myfile, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  return console.log(data);
});
