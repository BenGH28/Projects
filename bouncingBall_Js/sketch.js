let size = 20;
let divisor = 1.01
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
        for(let j = 0; j < balls.length; j++){
            if(i != j && balls[i].intersect(balls[j])){
                balls[i].rad /= divisor;
                balls[j].rad /= divisor;
            }
        }

    }
}