#!/usr/bin/node

const [, , firstArgument, secondArgument] = process.argv;

if (firstArgument || secondArgument) {
  console.log(`${firstArgument} is ${secondArgument}`);
} else {
  console.log(`${firstArgument} is ${secondArgument}`);
}
