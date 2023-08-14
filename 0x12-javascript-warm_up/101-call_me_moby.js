#!/usr/bin/node

const callMeBoy = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

module.exports.callMeBoy = callMeBoy;
