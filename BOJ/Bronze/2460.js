const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

let now = 0;
let max = 0;

for(let i =0; i<10; i++) {
  const [OUT, IN] = input[i].split(' ').map(Number);

  if(OUT) now -= OUT;
  now+= IN;

  if(now>max) {
    max = now;
  }

}

console.log(max);