const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');


const [V, E] = input[0].split(" ").map(e => parseInt(e));

const edges = [];
const realEdges = [];
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

edges.map(edge => {
  const [a, b, c] = edge;
  if (find(p, a) !== find(p, b)) {
    realEdges.push([a,b,c]);
    p = union(p, a, b);
    res += c;
  }
})


for(let i =0; i<input[E+1]; i++) {
  const [aa, bb] = input[i+E+2].split(" ").map(e => parseInt(e));
  
  console.log(getGap(aa,bb));
}

function getGap(aa,bb) {
  let p2 = new Array(V+1);
  for(let i =0; i<V+1; i++) {
    p2[i] = i;
  }
  let gap = 0;

  realEdges.map(edge => {
    const [a, b, c] = edge;
    if( find(p2,aa) == find(p2,bb)) {
      console.log("aa랑 bb 대표가 일치할때 비용",a,b,c) 
    }
    p2 = union(p2, a, b);
  })
  
  return gap;
}

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
