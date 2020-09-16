#!/usr/bin/bash
exports.callMeMoby = function (x, theFunction) {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
};
