#!/usr/bin/node

exports.esrever = function (list) {
  let reverseList = new Array();
  for (let i = list.length - 1; i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return reverseList;
}