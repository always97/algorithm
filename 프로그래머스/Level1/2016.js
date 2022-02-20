function solution(a, b) {
  let answer = '';
  const days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'];
  const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  let acc_day = 0;
  for (let i = 0; i < a - 1; i++) {
    acc_day += month[i];
  }
  acc_day += b - 1;


  return days[acc_day % 7];
}