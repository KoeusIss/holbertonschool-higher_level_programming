#!/usr/bin/node
const occurences = Number(process.argv[2]);
if (occurences) {
  for (let index = 0; index < occurences; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
