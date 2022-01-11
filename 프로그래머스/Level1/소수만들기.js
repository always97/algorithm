function isPrime(num) {
  for (let i = 2; i < num / 2; i++) {
    if (num % i == 0) return false;
  }
  return true;
}

function solution(nums) {
  let answer = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        let num = Number(nums[i] + nums[j] + nums[k]);
        if (isPrime(num)) answer++;
      }
    }
  }
  return answer;
}