#!/usr/bin/node

const [, , argTimes] = process.argv;
const times = parseInt(argTimes);

if (!isNaN(times)) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurencies');
}
