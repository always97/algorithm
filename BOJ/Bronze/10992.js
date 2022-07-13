const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const n = Number(input[0]);

for (let i = 1; i < n + 1; i++) {
  if (i == 1) {
    for (let j = 0; j < n - i; j++) {
      process.stdout.write(' ')
    }
    console.log('*');
  }
  else if (i == n) {
    for (let j = 0; j < n * 2 - 1; j++) {
      process.stdout.write('*')
    }
  }
  else {
    for (let j = 0; j < n - i; j++) {
      process.stdout.write(' ')
    }
    process.stdout.write('*')
    for (let j = 0; j < (i * 2 - 3); j++) {
      process.stdout.write(' ')
    }
    console.log('*');
  }
}