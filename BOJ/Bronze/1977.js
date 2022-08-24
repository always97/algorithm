const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');
const [a,b] = input;
let answer = [];
for(let i = a*1; i<=b*1 ; i++) {
  for(let j = 1; j<i/2; j++) {
    if(j*j == i) {
      answer.push(i);
      break;
    }
  }
}

let sum = 0;
answer.map((v)=> sum+=v);
if(answer.length) {
  console.log(sum);
  console.log(Math.min.apply(null,answer));
}else {
  console.log(-1);
}

const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const m = parseInt(input[0]);
const n = parseInt(input[1]);
const arr = [];
for (let i=Math.ceil(Math.sqrt(m)); i<= Math.floor(Math.sqrt(n)); i++) arr.push(i**2);
if (arr.length) {
    console.log(arr.reduce((acc, i) => acc + i, 0));
    console.log(arr[0]);
} else console.log(-1);