function solution(arr) {
  let answer = [];
  answer.push(arr[0]);
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] == arr[i - 1]) {
      continue;
    } else {
      answer.push(arr[i]);
    }
  }
  return answer;
}