const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [tc, ...arr] = input;
const [N,M] = tc.split(' ').map(i=>parseInt(i));
let board = arr[0].split(' ').map(i=>parseInt(i));
const ac_sum = new Array(board.length+1).fill(0);

board.forEach((v, i) => {
  ac_sum[i+1] = ac_sum[i] + v;
});
let result = [];

for(let i =1; i<=M; i++) {
  const [x,y] = arr[i].split(' ').map(i=>parseInt(i));
  result.push(ac_sum[y]-ac_sum[x-1]);
}
console.log(result.join('\n'));
