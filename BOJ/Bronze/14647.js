const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
// const input = fs.readFileSync(filePath).toString().split('\r\n');
const input = fs.readFileSync(filePath).toString().split('\n');

const [NM,...arr] = input;

const [N,M]= NM.split(' ').map(Number);

let arr2d = [];

for(let i=0;i<arr.length; i++) {
  let tmp = arr[i].split(' ');
  arr2d.push(tmp);
}
// 행 조사
let max_row = 0, sum_nine = 0;
for(let y = 0; y<N; y++) {
  let now_row = 0;
  for(let x=0; x<M; x++) {
    let nines = nineNum(arr2d[y][x]);
    now_row += nines;
    sum_nine += nines;
  }
  if(max_row<now_row) {
    max_row = now_row;
  }
}
// 열 조사
let max_col = 0;
for(let x = 0; x<M; x++) {
  let now_col = 0;
  for(let y=0; y<N; y++) {
    now_col += nineNum(arr2d[y][x]);
  }
  if(max_col<now_col) {
    max_col = now_col;
  }
}

function nineNum (x) {
  let cnt =0;
  for(let i =0; i<x.length; i++) {
    if(x[i] == '9') {
      cnt++;
    }
  }
  return cnt;
}

let max_nine = max_row>max_col ?  max_row : max_col;

console.log(sum_nine-max_nine);