const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc,...arr] = input;
const numbers = arr[0].split(' ');
const [n,max] = tc.split(' ');

let data = [];
let visited = new Array(max+1).fill(0);
for(let i =1; i<=n; i++) {
  let v = Number(numbers[i-1]);
  if(!visited[v]) {
    data.push({key:v,cnt:0,idx:i});
    visited[v] =1;
  }
}

for(let i =0; i<data.length;i++) {
  for(let j =0; j<n;j++) {
    if(data[i].key == numbers[j]) {
      data[i].cnt++;
    }
  }
}

function compareNum(a,b) {
  if(a.cnt > b.cnt) {
    return -1;
  }
  if(a.cnt < b.cnt) {
    return 1;
  }
  if(a.cnt == b.cnt) {
    if(a.idx > b.idx) {
      return 1;
    }
    return -1;
  }
  return 0;
}

data.sort(compareNum);

let result = '';

for(let i =0; i<data.length; i++) {
  for(let j = 0; j<data[i].cnt; j++) {
    result+= (data[i].key+' ');
  }
}

console.log(result);
