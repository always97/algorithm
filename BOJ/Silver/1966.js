const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

[tc, ...arr] = input;

function solution() {
  let idx = 0;
  for(let i = 0; i<tc; i++) {
    [num, who] = arr[idx++].trim().split(' ');
    
  }
}