const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n').map(i => parseInt(i));

const sum = input.reduce((acc,cur)=>{
  return acc+cur*1;
},0); 

let gap = Math.abs(100 - sum);

let result1, result2;
for(let i = 0; i<8; i++) {
  for(let j=i+1; j<9; j++) {
    if(input[i]+input[j] == gap) {
      result1 = input.filter((v)=> v != input[i]);
      result2 = result1.filter((v)=> v != input[j]);
      break;
    }
  }
}
result2.sort((a,b)=> a-b).map((v)=>console.log(v));

let nums = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(i => parseInt(i));
let arr;
for (let i=0; i<8; i++) {
    for (let j=i+1; j<9; j++) {
        if (nums.reduce((sum, item) => sum + item, 0) - 100 === nums[i] + nums[j] ) {
            arr = nums.filter(item => item !== nums[i] && item !== nums[j]);
            break;
        }
    }
    if (arr) break; 
}
arr.sort((a, b) => a - b);
for(let i=0; i<7; i++) console.log(arr[i]);
