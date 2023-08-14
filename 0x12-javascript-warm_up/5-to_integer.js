#!/usr/bin/node

const [, , firstArgument] = process.argv;
const myNum = parseInt(firstArgument);

if (!isNaN(myNum)) {
  console.log(`My number: ${myNum}`);
} else {
  console.log('Not a number');
}
