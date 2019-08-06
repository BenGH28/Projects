let size = 100;
let balls = new Array(size);
function setup(){
    createCanvas(600, 400);
    for(let i = 0; i < balls.length; i++){
        balls[i] = new Ball();
    }
}
function draw(){
    background(240,230, 222);
    for(let i = 0; i < balls.length; i++){
        balls[i].show();
        balls[i].move();
        balls[i].bounce();
        //balls[i].intersect(balls[i+1])

    }
}