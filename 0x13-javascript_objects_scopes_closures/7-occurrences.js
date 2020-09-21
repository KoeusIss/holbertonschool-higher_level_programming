#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurencesCounter = 0;
  for (const item of list) {
    if (item === searchElement) {
      occurencesCounter++;
    }
  }
  return occurencesCounter;
};
