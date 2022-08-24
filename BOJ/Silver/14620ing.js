const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\r\n');


// 1. (x,y)를 모두 모아라 arr에
// 2. arr에서 3개 고르기 조합
// 3. i j k 겹치는지 확인
// 4. 겹치지 않으면 좌표값에 비용 다 더하기


const [n,...board] = input;
let list = [];

for(let i=0;i<n;i++) {
  for(let j=0;j<n;j++) {
    list.push([i,j]);
  }
}
console.log(list.length);

let threeList = [];

function calc(a,b,c) {
  
}

for(let i =0; i<list.length; i++) {
  for(let j =i+1; j<list.length; j++) {
    for(let k =j+1; k<list.length; k++) {
      threeList.push([list[i],list[j],list[k]]);
    }
  }
}
console.log(threeList);






let dx = [1,-1,0,0];
let dy = [0,0,1,-1];
// for(let y=0;y<n;y++) {
//   for(let x=0;x<n;x++) {
//     let nX = x+dx[x];
//     let nY = y+dy[y];
//     if(nX>n || nY>n)
//   }
// }