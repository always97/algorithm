const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc,...arr] = input;

let store = new Array(10001).fill(0);


for(let i =0; i<tc;i++) {
  store[Number(arr[i])]++;
}

for(let i =0; i<10001; i++) {
  if(store[i]) {
    for(let j = 0; j<store[i]; j++) {
      console.log(i);
    }
  }
}

