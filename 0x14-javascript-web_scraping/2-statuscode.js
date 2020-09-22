#!/usr/bin/node
const request = require('request');
const theUrl = process.argv[2];
request.get(theUrl)
  .on('response', response => {
    console.log(`code: ${response.statusCode}`);
  });
