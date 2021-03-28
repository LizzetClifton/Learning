//practice from online tutorial

var maxCircleSize = 30;
var phase = 0;
var speed = 0.04;
var numRows = 10;
var numCols = 16;
var numStrands = 1;
colorA;
colorB;

function setup() {
  createCanvas(windowWidth, windowHeight);
  colorA = color(253, 204, 120);
  colorB = color(255, 109, 141);
}

function draw() {
  background(6, 72, 73);
  strokeWeight(0);
  phase = frameCount * speed;

  for(var s = 0; s < numStrands; s += 1) {
    var strandPhase = phase + map(s, 0, numStrands, 0, TWO_PI);

    for(var col = 0; col < numCols; col += 1) {
      var colOffset = map(col, 0, numCols, 0, TWO_PI);
      var x = map(col, 0, numCols, 50, width);

      for(var row = 0; row < numRows; row += 1) {
        var y = (height/2 + row * 40 + sin(strandPhase + colOffset) * 70) - 180;

        var sizeOffset = (cos(strandPhase - (row / numRows) + colOffset) + 1) * 0.3;

        var circleSize = sizeOffset * maxCircleSize;

        fill(lerpColor(colorA, colorB, row / numRows));
        ellipse(x, y, circleSize, circleSize);
      }
    }
  }
}
