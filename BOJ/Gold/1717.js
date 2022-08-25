// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// let input = [];

// rl.on('line', function (line) {
//   input.push(line)
// })
//   .on('close', function () {
//   console.log(input);
//   process.exit();
// });
//------------------------------------------------------------------------------

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [n,...arr] = input;

const [N,M] = n.split(' ').map(i=>parseInt(i));

let p = new Array(1000001);

for(let i =0; i<=N; i++) {
  p[i] = i;
}
console.log(p);
for(let i =0; i<M; i++) {
  const[cmd,a,b] = arr[i].split(' ').map(i=> parseInt(i));
  if(cmd == 0) {
    union(a,b);
  }else {
    if(find(a)==find(b)) {
      console.log("YES")
    }else {
      console.log("NO")
    }
  }
}

function union (a,b) {
  p[find(b)] = a;
}
function find(a) {
  if(a == p[a]) {
    return a;
  } 
  
  p[a] = find(p[a]);
  return find(p[a]);
}