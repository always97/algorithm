const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [stairNum, ...stepPoint] = input;
let answer = Number(stepPoint[0]) + Number(stepPoint[stairNum - 1]);

let i = 1;

// 풀이중

console.log(answer);

