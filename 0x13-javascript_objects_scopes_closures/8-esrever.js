#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  const len = list.length - 1;

  for (let i = len; i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return reverseList;
};
