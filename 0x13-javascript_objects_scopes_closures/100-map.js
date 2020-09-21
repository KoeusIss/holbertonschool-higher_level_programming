#!/usr/bin/node
const { list } = require('./100-data');
const newList = list.map((index, value) => index * value);
console.log(list);
console.log(newList);
