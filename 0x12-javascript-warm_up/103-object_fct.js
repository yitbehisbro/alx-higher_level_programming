#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr (a) {
  return a + 1;
}
{...myObject, incr: function () { return this.value++ };

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
