#!/usr/bin/node

const [, , firstArgument] = process.argv;

if (!firstArgument) {
  console.log('No argument');
} else {
  console.log(firstArgument);
}
