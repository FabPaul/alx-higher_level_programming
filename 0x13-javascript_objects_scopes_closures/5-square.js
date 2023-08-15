#!/usr/bin/node

// Class Square that defines a square and inherits from Rectangle

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      return; // if ther is an empty class, print nothing
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    if (!this.width || !this.height) {
      return;
    }

    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super (size, size);
  }
}

module.exports = { Rectangle, Square };
