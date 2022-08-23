const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [n,tc, ...arr] = input;

let answer = new Map();
for(let i =0; i<=n;i++) {
  answer.set(i,[]);
}

for(let i = 0; i<tc; i++) {
  const [a,b] = arr[i].split(' ');
  answer.get(Number(a)).push(Number(b));
  answer.get(Number(b)).push(Number(a));
}

let visit = new Array(100).fill(0);

function bfs(start) {
  let q = [];
  let cnt = 0;
  q.push(start);
  while(q.length) {
    let p =q.shift(); 
  
    if(!visit[p]) {
      answer.get(p).map((v)=> {
        q.push(v);
      })
      visit[p] = 1;
      cnt++;
    }
  }
  return cnt;
}

console.log(bfs(1)-1);


