const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc,...arr] = input;

for(let i =0; i<tc; i++) {
  let answer = '';
  const [count, str] = arr[i].split(' ');
  for(let j = 0; j<str.length; j++) {
    answer += str[j].repeat(count);
  }
  console.log(answer);
}