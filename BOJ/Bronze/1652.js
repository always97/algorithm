const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc,...arr] = input;
let 가로 = 0, 세로 = 0;
for(let i = 0; i<tc; i++) {
  let cnt = 0;
  for(let j = 0;j<tc; j++) {
    if(arr[i][j] == '.') {
      cnt++;
    }else if (arr[i][j] == 'X') {
      if(cnt >=2) {
        가로++;
      }
      cnt = 0;
    }
  }
  if(cnt>=2) 가로++;
}
for(let i = 0; i<tc; i++) {
  let cnt = 0;
  for(let j = 0;j<tc; j++) {
    if(arr[j][i] == '.') {
      cnt++;
    }else if (arr[j][i] == 'X') {
      if(cnt >=2) {
        세로++;
      }
      cnt = 0;
    }
  }
  if(cnt>=2) 세로++;
}

let answer = `${가로} ${세로}`;
console.log(answer);
