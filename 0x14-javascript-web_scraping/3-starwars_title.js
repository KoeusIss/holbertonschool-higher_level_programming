#!/usr/bin/node
const request = require('request');
const episodeId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api';
request(apiUrl + `/films/${episodeId}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
