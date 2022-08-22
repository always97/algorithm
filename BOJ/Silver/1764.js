const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [a,b] = input[0].split(' ');
const [tc, ...arr] = input;

arr.sort();
let answer = [];

for(let i = 0; i<arr.length-1; i++) {
  if(arr[i] == arr[i+1]) {
    answer.push(arr[i]);
  }
}

console.log(answer.length);
answer.map((v)=> console.log(v));


