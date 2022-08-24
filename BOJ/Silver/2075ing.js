const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\r\n');

const [N,...arr] = input;
let answer = arr[0].split(' ');
answer.sort();
for(let i = 1; i<N; i++) {
  let num = arr[i].split(' ');
  console.log(num);
}

