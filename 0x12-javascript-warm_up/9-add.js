#!/usr/bin/node

const [, , firstArgument, secondArgument] = process.argv;
const a = parseInt(firstArgument);
const b = parseInt(secondArgument);

function add (a, b) {
  return a + b;
}

if (!isNaN(a) && !isNaN(b)) {
  console.log(add(a, b));
} else {
  console.log('NaN');
}
