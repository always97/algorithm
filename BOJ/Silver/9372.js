const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [tc,...arr] = input;
for(let i = 0; i<tc; i++) {
  const [n,m] = arr[0].split(' ').map(i=>parseInt(i));

}

console.log(n,m);