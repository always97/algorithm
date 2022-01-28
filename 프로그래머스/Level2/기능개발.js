function solution(progresses, speeds) {
  let answer = [];
  let day;
  let last_day = Math.floor((99 - progresses[0]) / speeds[0]) + 1;
  let cnt = 1;
  for (let i = 1; i < progresses.length; i++) {
    day = Math.floor((99 - progresses[i]) / speeds[i]) + 1;

    if (last_day < day) {
      answer.push(cnt);
      cnt = 1;
      last_day = day;
    } else {
      cnt++;
    }

    if (i == progresses.length - 1) {
      answer.push(cnt);
    }
  }

  return answer;
}