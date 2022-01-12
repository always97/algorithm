function solution(lottos, win_nums) {
  let answer = [];
  let win_count = 0;
  let zero_count = lottos.filter(n => n == 0).length;

  for (let i = 0; i < lottos.length; i++) {
    if (win_nums.includes(lottos[i])) win_count++;
  }

  const total = win_count + zero_count;

  let 최고등수 = 7 - total < 7 ? 7 - total : 6;
  let 최저등수 = (7 - win_count) < 7 ? 7 - win_count : 6;

  answer.push(최고등수);
  answer.push(최저등수);

  return answer;
}