/* 백준에서 node언어 사용하여 문제풀이 하기 위한 기본 형식 (입력, 출력) 예제 */

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

console.log(input);

const s = input[0].split(' ');
const t = input[1].split(' ');


const answer = solution(s, t);

function solution(s, t) {
  let sumS = 0;
  let sumT = 0;
  for (let i = 0; i < s.length; i++) {
    sumS += Number(s[i]);
    sumT += Number(t[i]);
  }
  return (sumS > sumT) ? sumS : sumT;
}

console.log(answer);

