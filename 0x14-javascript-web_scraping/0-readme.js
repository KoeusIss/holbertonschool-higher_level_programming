#!/usr/bin/node
const fs = require('fs');
const theFile = process.argv[2];
const stream = fs.createReadStream(theFile, 'utf-8');
stream.on('error', error => {
  console.log(error);
})
  .on('data', data => {
    console.log(data);
  });
