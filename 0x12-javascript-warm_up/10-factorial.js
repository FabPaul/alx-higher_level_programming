#!/usr/bin/node

const [, , factorialNumber] = process.argv;
const num = parseInt(factorialNumber);

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0 || x === 1) {
    return 1;
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(`${factorial(num)}`);
