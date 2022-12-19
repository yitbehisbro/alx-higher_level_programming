#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr (a) {
  return a + 1;
}

incr(myObject.value);
console.log(myObject);
incr(myObject.value);
console.log(myObject);
incr(myObject.value);
console.log(myObject);
