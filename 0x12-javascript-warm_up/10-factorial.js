#!/usr/bin/node
function factorial (f) {
  if ((Number.isNaN(f)) || (f === 1)) {
    return 1;
  }
  return factorial(f - 1) * f;
}

console.log(factorial(parseInt(process.argv[2])));
