const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\r\n');

console.log(input);
let select = new Array(10).fill(0);
// let answer = new Array(7).fill(0);

let result =[];
let sum = 0;
function rec(idx,n) {
  if(n == idx) {
    for(let i = 0; i<n; i++) {
      if(select[i] == 1){
        result.push(input[i]*1)
        sum += input[i]*1;
      }
    }
    if(sum== 100) {
      console.log(result);
    }
  }
  select[idx] = 0;
  rec(idx+1,n);
  select[idx] = 1;
  rec(idx+1,n);
  
}

rec(0,7);