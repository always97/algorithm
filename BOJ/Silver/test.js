const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

let arr = [1,7,9,10,12];
let select = new Array(5).fill(0);
let answer = new Array(3).fill(0);
let N = 5;
let r = 3;

function perm(N,r,idx) {
  if(r==idx) {
    console.log(answer);
    return;
  }
  for(let i = 0; i<N; i++) {
    if(select[i]==0) {
      answer[idx] = arr[i];
      select[i] = 1;
      perm(N,r,idx+1);
      select[i] = 0;
    }
  }
}

perm(N,r,0);

// for(let a = 0; a<3; a++) {
//   for(let b = 0; b<3; b++) {
//     if(a==b) continue;
//     for(let c = 0; c<3; c++) {
//       if(c==a || c==b) continue;
//       console.log(arr[a] + " "+arr[b]+" "+arr[c]);
//     }
//   }
// }

// function solve (select,arr) {
//   let answer = '';
//   for(let i = 0; i<4; i++) {
//     if(select[i] == 1){
//       answer += (arr[i]+' ')
//     }
//   }
//   console.log(answer);
// }

let answer = '';
let cnt = 0;
function rec(idx,n) {
  if(n == idx) {
    for(let i = 0; i<n; i++) {
      if(select[i] == 1){
        answer += (arr[i]+' ')
      }
    }
    let tmp = answer.split(' ');
    let sum = 0;
    for(let i = 0;i<tmp.length; i++) {
      sum += (tmp[i]*1);
    }
    if(sum == 0) {
      console.log(answer);
      cnt++;
    }
    answer='';
    return;
  }
  select[idx] = 0;
  rec(idx+1,n);
  select[idx] = 1;
  rec(idx+1,n);
  
}

// rec(0,10);
// console.log(cnt);


// for(let a = 0; a<2; a++){
//   select[0] = a;
//   for(let b = 0; b<2; b++){
//     select[1] = b;
//     for(let c = 0; c<2; c++){
//       select[2] = c;
//       for(let d = 0; d<2; d++){
//         select[3] = d;
//         solve(select,arr);
//       }
//     }
//   }  
// }