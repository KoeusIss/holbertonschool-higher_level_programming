#!/usr/bin/node
const array = process.argv.slice(2).map(function (x) {
  return Number(x);
});
array.sort(function (a, b) {
  return a - b;
});
if (array.length > 1) {
  console.log(array[array.length - 2]);
} else {
  console.log(0);
}
