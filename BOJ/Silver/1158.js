const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim();

const [a, b] = input.split(' ');

let q = [];
for(let i = 1; i<=a; i++) {
  q.push(i);
}
let answer = "<";
while(q.length) {
  for(let i =0;i<b-1; i++) {
    q.push(q.shift());
  }
  answer+= q.shift();
  if(q.length) answer+=", ";
  else answer+= '>';
}

console.log(answer);