#!/usr/bin/node
const array = process.argv.slice(2).map(function (x) {
  return Number(x);
});
if (array.length > 1) {
  console.log(array.sort()[array.length - 2]);
} else {
  console.log(0);
}
