const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [tc, ...arr] = input;
let answer = [];

for(let i =0; i<tc; i++) {
  let str = arr[i].split('\r')[0];
  let value = 0;
  for(let j = 0; j<str.length; j++) {
    if(value<0) break;
    str[j] == '(' ?  value ++ : value --;
  }
  value ? answer.push("NO") : answer.push("YES")
}

answer.map((result)=> console.log(result));