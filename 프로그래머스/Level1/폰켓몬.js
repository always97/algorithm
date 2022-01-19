function solution(nums) {
  let answer = 0, arr = Array.from({ length: 200001 }, () => 0);
  nums.map(n => { if (!arr[n]++) ++answer; });
  return Math.min(nums.length / 2, answer);
}