#!/usr/bin/node

const [, , squareSize] = process.argv;
const square = parseInt(squareSize);

if (!isNaN(square)) {
  for (let i = 0; i < square; i++) {
    let line = '';
    for (let j = 0; j < square; j++) {
      line += 'x';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
