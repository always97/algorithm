function solution(numbers) {
  let answer = [];
  const arr = Array.from({ length: 200 }, () => 0);
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let sum = numbers[i] + numbers[j];
      arr[sum]++;
    }
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i]) {
      answer.push(i);
    }
  }
  return answer;
}