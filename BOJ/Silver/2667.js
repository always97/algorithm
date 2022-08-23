const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [tc,...arr] = input;

let arr2 = []
for(let y=0; y<tc; y++) {
  let tmp = []
  for(let x=0;x<tc;x++) {
    tmp.push(arr[y][x])
  }
  arr2.push(tmp)
}
// console.log(arr2);

let answer = [];

for(let y=0; y<tc; y++) {
  for(let x=0;x<tc;x++) {
    if(arr2[y][x] == '1') {
      let num = bfs(x,y);
      answer.push(num);
    }
  }
}


function bfs(x,y) {
  let q = [];
  let cnt = 1;
  q.push([x,y]);
  arr2[y][x] = '0';
  let dx = [1,-1,0,0];
  let dy = [0,0,-1,1];

  while(q.length) {
    let p = q.shift();
    let xx = p[0];
    let yy = p[1];
    for(let i = 0; i<4; i++) {
      let nX = xx + dx[i];
      let nY = yy + dy[i];
      if(nX < 0 || nY < 0 || nX >=tc || nY>=tc) {
        continue;
      }
      if(arr2[nY][nX] == '1') {  
        arr2[nY][nX] = '0';  
        q.push([nX,nY]);  
        cnt++;
      }
    }
  }
  return cnt;
}

console.log(answer.length);
answer.sort((a, b) => a - b).map((v)=>console.log(v));