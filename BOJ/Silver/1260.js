const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [data, ...arr] = input;
const [n,m,start] = data.split(' ');
let answer = new Map();
for(let i =0; i<=n;i++) {
  answer.set(i,[]);
}

for(let i = 0; i<m; i++) {
  const [a,b] = arr[i].split(' ');
  answer.get(Number(a)).push(Number(b));
  answer.get(Number(b)).push(Number(a));
}

function bfs(start) {
  let q = [];
  let visit = new Array(100).fill(0);
  let result = [];
  q.push(start);
  
  while(q.length) {
    let p =Number(q.shift()); 
    if(!visit[p]) {
      answer.get(p).map((v)=> {
        q.push(v);
      })
      visit[p] = 1;
      result.push(p);
    }
  }
  return result;
}

let visit1 = new Array(100).fill(0);
let result1 = [];
function dfs(start) {
  
  if(visit1[start]) {
    return;
  }
  visit1[start] = 1;
  result1.push(start);
  answer.get(start).map((v)=> {
    if(!visit1[v]) {
      dfs(v);
    }
  })

  return result1;
}
// function dfs(start) {
//   let stack = [];
//   let result = [];
//   let visit = new Array(100).fill(0);
//   stack.push(start);
//   while(stack.length) {
//     let p =Number(stack.pop()); 
//     if(!visit[p]) {
//       result.push(p);
//       visit[p] = 1;
//       answer.get(p).map((v)=> {
//         if(!visit[v])
//           stack.push(v);
//       })
//     }
//   }
//   return result;
// }

let result_dfs = dfs(Number(start));
let result_bfs = bfs(Number(start));

let rd = '';
let rb = '';
for(let i =0;i<n;i++) {
  rd+=result_dfs[i]+' ';
  rb+=result_bfs[i]+' ';
}
console.log(rd);
console.log(rb);
