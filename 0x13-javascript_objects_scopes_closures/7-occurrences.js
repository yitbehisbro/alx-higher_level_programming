#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const counter = {};
  for (const i of list) {
    if (i === searchElement) {
      counter[i] = counter[i] ? counter[i] + 1 : 1;
    }
  }
  console.log(counter);
}
