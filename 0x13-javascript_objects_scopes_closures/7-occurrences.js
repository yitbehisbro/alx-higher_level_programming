#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let elem = 0; elem < list.length; elem++) {
    if (list[elem] === searchElement) {
      counter++;
    }
  }
  return counter;
}
