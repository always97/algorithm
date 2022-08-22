const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc,...arr] = input;
let 가로 = 0, 세로 = 0;
for(let i = 0; i<tc; i++) {
  let str = arr[i].split('\r')[0];
  for(let j = 0;j<tc; j++) {
    가로 += (arr[i][j] == '.' && arr[i][j + 1] == '.' && arr[i][j + 2] == 'X') ? 1 : 0;
    세로 += (arr[j][i] == '.' && arr[j + 1][i] == '.' && arr[j + 2][i] == 'X') ? 1 : 0;
  }
}
console.log(가로,세로);
