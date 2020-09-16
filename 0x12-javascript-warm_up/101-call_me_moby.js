#!/usr/bin/bash
export function (x, theFunction) {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
};
