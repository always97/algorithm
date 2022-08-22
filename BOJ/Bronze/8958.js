const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [tc, ...arr] = input;
let sum  = 0, bonus = 1;

arr.map((str)=> {
  for(let i = 0; i<str.length; i++) {
    if(str[i] == 'O') sum += bonus++;
    else bonus = 1;
  }
  console.log(sum);
  sum = 0;
})

