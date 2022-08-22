
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc, ...arr] = input;

let coord = [];
let answer = 0;
for(let i = 0; i<arr.length; i++) {
  arr[i] = arr[i].split('\r')[0];
  for(let j = 0; j<arr[i].length; j++) {
    if(arr[i][j] !== '.') {
      coord.push([i,j]);
    }
  }
}
let combination = [];
for(let i = 0; i<coord.length-2; i++) {
  for(let j = i+1; j<coord.length-1; j++) {
    for(let k = j+1; k<coord.length; k++) {
      combination.push([coord[i],coord[j],coord[k]]);
    }
  }
}

for(let i =0; i<combination.length; i++) {
  let a=combination[i][0];
  let b=combination[i][1];
  let c=combination[i][2];
  if((b[1]-c[1])*(a[0]-b[0]) == (b[0]-c[0])*(a[1]-b[1])) {
    answer+=1;
  }
  
}

console.log(answer);

