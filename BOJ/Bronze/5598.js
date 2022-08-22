const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

let str = input[0];
let answer = '';

for(let i = 0; i<str.length;i++) {
  let code = str[i].charCodeAt(0)-3;

  let newCode = code<65 ? code+26 : code;

  answer+=(String.fromCharCode(newCode));
}

console.log(answer);
