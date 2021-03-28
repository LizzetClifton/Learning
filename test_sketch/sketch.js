var circles = [];

function setup() {

  createCanvas(windowWidth, windowHeight);

  for (var i=0; i<10; i++) {
    var x = random(0, windowWidth);
    var y = random(0, windowHeight);
    circles.push(new Circle(x, y));
  }
}

function mousePressed() {
  for (var i = 0; i < circles.length; i++) {
    circles[i].clicked();
  }
}

function draw() {
  background(150, 150, 150);

  for (var i = 0; i < circles.length; i ++)  {
    circles[i].display();
  }
}

class Circle {
  constructor(tempX, tempY) {
    this.x = tempX;
    this.y = tempY;
    this.col = color(255, 100);
  }

  display() {
    strokeWeight(0);
    fill(this.col);
    ellipse(this.x, this.y, 100, 100);
  }

  clicked() {
    var d = dist(mouseX, mouseY, this.x, this.y);
    if (d<50) {
      this.col = color(255, 0, 200);
    }
  }
}
