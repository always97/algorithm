const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');


const [V, E] = input[0].split(" ").map(e => parseInt(e));

const edges = [];
let p = new Array(V+1);
let res = 0;

for (let i = 0; i <= V; i++) {
  p[i] = i;
}
for (let i = 0; i < E; i++) {
  const [a, b, c] = input[1 + i].split(" ").map(e => parseInt(e));
  edges.push([a, b, c]);
}

edges.sort((a, b) => a[2] - b[2]);  // 가중치로 정렬

let maxCost = 0;
edges.map(edge => {
  const [a, b, c] = edge;
      if (find(p, a) !== find(p, b)) {
          maxCost = Math.max(maxCost, c);
          p = union(p, a, b);
          res += c;
      }
})
console.log(res-maxCost);



function find(p, x) {
  if (p[x] !== x) {
      p[x] = find(p, p[x]);
  }
  return p[x];
}

function union(p, a, b) {
  a = find(p, a);
  b = find(p, b);
  if (a < b) {
      p[b] = a;
  } else {
      p[a] = b;
  }
  return p;
}