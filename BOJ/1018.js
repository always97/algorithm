/* tag : BruteForce */

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const whiteFirst = [
  "WBWBWBWB",
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW'
];
const blackFirst = [
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB'
];

function whiteFirstChange(x, y, inputBoard) {
  let cnt = 0;
  for (let i = x; i < x + 8; i++) {
    for (let j = y; j < y + 8; j++) {
      if (whiteFirst[i - x][j - y] != inputBoard[i][j]) cnt++;
    }
  }
  return cnt;
}

function blackFirstChange(x, y, inputBoard) {
  let cnt = 0;
  for (let i = x; i < x + 8; i++) {
    for (let j = y; j < y + 8; j++) {
      if (blackFirst[i - x][j - y] != inputBoard[i][j]) cnt++;
    }
  }
  return cnt;
}

function solution(input) {
  [size, ...board] = input;
  [row, col] = size.split(' ');
  board = board.map(str => str.trim('\r').split(''));


  let answer = 64;
  let tmp = 64;
  for (let i = 0; i + 7 < row; i++) {
    for (let j = 0; j + 7 < col; j++) {
      tmp = Math.min(whiteFirstChange(i, j, board), blackFirstChange(i, j, board));
    }
    if (tmp < answer) answer = tmp;
  }

  return answer;
}

console.log(Number(solution(input)));