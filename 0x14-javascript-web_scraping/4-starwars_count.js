#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api';
request(apiUrl + '/films', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let counter = 0;
    for (const movie of results) {
      if (movie.characters.find(value => value.endsWith('18/'))) {
        counter++;
      }
    }
    console.log(counter);
  }
});
