const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N,M] = input[0].split(' ').map(Number);

const arr = input[1].split(' ').map(Number);

arr.sort((a,b)=> a-b);

let now = 2000000000;
let height = 0;

for(let i = arr[0]; i<arr[N-1]; i++) {
  let sum = 0;
  arr.map((v) => {
    if(v-i >0) {
      sum += v-i
    }
  })
  if(sum>=M) {
    if(now >= sum) {
      now = sum;
      height= i;
    }
  }
}

console.log(height);