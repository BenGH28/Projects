class Ball {
  constructor() {
    this.x = random(0, width);
    this.y = random(0, height);
    this.xspeed = random(5);
    this.yspeed = random(5);
    this.rad = 15;
    this.r = 0;
    this.b = 0;
    this.g = 0;
  }
  changeColour() {
    this.r = random(0, 200);
    this.b = random(0, 200);
    this.g = random(0, 200);
  }
  move() {
    this.x += this.xspeed;
    this.y += this.yspeed;
  }
  show() {
    stroke(this.r, this.g, this.b);
    strokeWeight(4);
    noFill();
    ellipse(this.x, this.y, this.rad * 2, this.rad * 2);
  }
  bounce() {
    if (this.x >= width || this.x <= 0) {
      this.xspeed = -this.xspeed;
      this.changeColour();
    }
    if (this.y >= height || this.y <= 0) {
      this.yspeed = -this.yspeed;
      this.changeColour();
    }
  }
  intersect(other) {
    let d = dist(this.x, this.y, other.x, other.y);
    if (d < this.rad + other.rad) {
      return true;
    } else {return false;}
  }
  collide(){
      this.xspeed *= -1;
      this.yspeed *= -1;
  }
}
