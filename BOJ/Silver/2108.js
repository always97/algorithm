const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const [tc, ...nums] = input;
let sum = 0;
let average; // 평균 = average
let median = ((nums[tc / 2] + nums[(tc / 2) + 1]) / 2);  // 중앙값 = median
let mode = Array.from({ length: tc }, x => 0);  // 최빈값 = mode

console.log(median);

const sortNums = nums.sort((a, b) => a - b);


for (let i = 0; i < tc; i++) {
  mode[Number(nums[i])]++;
  sum += Number(nums[i]);
}
let maxIdx = 0;
mode.map(i => {
  if (mode[maxIdx] < mode[i]) {
    maxIdx = i;
  }
})
average = sum / tc;
console.log("평균 :", average);
console.log("중앙값 : ", median);
console.log("최빈값 : ", maxIdx);
