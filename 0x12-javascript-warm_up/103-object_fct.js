#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr () {
  let x = parseInt(myObject.value) + 1;
  myObject.value = x;
}

incr();
console.log(myObject);
incr();
console.log(myObject);
incr();
console.log(myObject);
