#!/usr/bin/node
const fs = require('fs');
const theFile = process.argv[2];
const theString = process.argv[3];
const stream = fs.createWriteStream(theFile, 'utf-8');
stream.write(theString);
stream.on('error', error => {
  console.log(error);
});
