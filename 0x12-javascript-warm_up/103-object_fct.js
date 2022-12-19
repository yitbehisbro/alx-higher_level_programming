#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr () {
  parseInt(myObject.value);
  myObject.value++;
}

incr();
console.log(myObject);
incr();
console.log(myObject);
incr();
console.log(myObject);
