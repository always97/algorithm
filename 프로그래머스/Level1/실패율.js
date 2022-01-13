function solution(N, stages) {
  let answer = [];
  let fail_percent = [];

  for (let i = 1; i <= N; i++) {
    fail_percent.push(
      {
        percent: (stages.filter(n => n == i).length / stages.filter(n => n >= i).length),
        idx: i
      }
    )
  }
  let sortArr = fail_percent.sort(function (a, b) {
    return b.percent - a.percent;
  });
  sortArr.map((n) => answer.push(n.idx));

  return answer;
}