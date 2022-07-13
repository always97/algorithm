// 오븐시계

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');
let [hour, minute] = input[0].split(' ');
let takeTime = input[1];

let answer = '';

let sum = Number(minute)+Number(takeTime);


if( sum > 59) {
    let t = parseInt(sum/60);
    hour = Number(hour)+t;
    sum -= t*60;
}
if(hour > 23) hour -= 24;
answer = hour + " " + sum;

console.log(answer);


