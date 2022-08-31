const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const [a,b] = fs.readFileSync(filePath).toString().trim().split(' ');


function toRev (x) {
  x+='';
  let tmp = '';
  for(let i = x.length-1; i>=0; i--) {
    tmp += x[i];
  }
  return Number(tmp);
}

console.log(toRev(toRev(a)+toRev(b)));
