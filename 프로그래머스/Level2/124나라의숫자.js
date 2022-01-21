function solution(n) {
  let answer = '';
  let otf = ['4', '1', '2'];
  while (n) {
    let c = n % 3;
    if (c == 0) {
      --n;
    }
    n = Math.floor((n) / 3);
    answer = otf[c] + answer;
  }
  return answer;
}