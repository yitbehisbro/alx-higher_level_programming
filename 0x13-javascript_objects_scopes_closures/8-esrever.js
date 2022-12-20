#!/usr/bin/node

exports.esrever = function (list) {
  let reverseList = [];
  const len = list.length - 1;

  for (let i = len; i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return reverseList;
}
