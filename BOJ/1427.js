
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

let answer = '';
const arr = [];
const number = input[0];

for (let i = 0; i < number.length; i++) {
  arr.push(number[i]);
}

arr.sort((a, b) => b - a);

arr.map(num => answer += num);

console.log(answer);

