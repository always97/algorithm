const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');


// let n = 3;
// let ans = new Array(10);
// function rec(idx,n) {
//   if(idx == n) {
//     console.log(ans);
//     return
//   }
//   for(let i = 0; i<n; i++) {
//     ans[idx] = i;
//     rec(idx+1,n);
//   }
// }

// rec(0,n);

// ----------------------------------------------------
const [n, ...arr] = input;

let answer = new Map();
for(let i =0; i<9;i++) {
  answer.set(i,[]);
}
console.log(answer)


for(let i = 0; i<n; i++) {
  const [a,b] = arr[i].split(' ');
  console.log(a,b)
  answer.get(Number(a)).push(Number(b));
  answer.get(Number(b)).push(Number(a));
}
console.log(answer);

let visit = new Array(10).fill(0);

// function bfs(start) {
//   let q = [];  // 큐
//   visit[start] = 1; // 시작점 방문표시
//   q.push(start); // 시작점 큐에 삽입
//   console.log(start); // 시작점 출력
//   while(q.length) {
//     answer.get(q.shift()).map((v)=> {  // 큐에서 가져온 점과 연결된 모든 점 탐색
//       if(!visit[v]) { // 방문하지 않았다면
//         visit[v] = 1; // 방문표시
//         q.push(v); // 큐에 삽입
//         console.log(v); // 출력
//       }
//     })
//   }
// }

// bfs(3);

function dfs(start) {
  console.log(start);
  visit[start] = 1;
  answer.get(start).map((v)=> {
    if(!visit[v]) {
      dfs(v);
    }
  })
}

dfs(2)