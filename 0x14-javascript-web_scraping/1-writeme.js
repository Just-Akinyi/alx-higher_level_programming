#!/usr/bin/node
const fs = require('fs');
const myfile = process.argv[2];
fs.readFile(myfile, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }else{
  console.log(data);
}});
