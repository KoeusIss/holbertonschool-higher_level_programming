#!/usr/bin/node
const size = Number(process.argv[2]);
if (size) {
  for (let index = 0; index < size; index++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
