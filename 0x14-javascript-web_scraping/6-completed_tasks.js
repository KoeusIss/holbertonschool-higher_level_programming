#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const result = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (!result[todo.userId]) {
          result[todo.userId] = 1;
        } else {
          result[todo.userId]++;
        }
      }
    }
    console.log(result);
  }
});
