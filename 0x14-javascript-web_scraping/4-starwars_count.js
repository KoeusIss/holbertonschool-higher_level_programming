#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api';
request(apiUrl + '/films', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    for (const row of JSON.parse(body).results) {
      if (row.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        counter++;
      }
    }
    console.log(counter);
  }
});
