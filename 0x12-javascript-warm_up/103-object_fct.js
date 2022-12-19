#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr () {
  myObject.value = myObject.value + 1;
}

incr();
console.log(myObject);
incr();
console.log(myObject);
incr();
console.log(myObject);
