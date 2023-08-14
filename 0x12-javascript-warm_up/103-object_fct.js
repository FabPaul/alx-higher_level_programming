#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const incr = function (x) {
    return x + 1;
  };

  theFunction(incr(number));
};
