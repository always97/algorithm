function solution(n, lost, reserve) {
  let 체육복있는학생수 = n - lost.length; // 전체학생에서 도난당한학생을 제외한 수.
  const 체육복진짜없는학생들 = [];

  lost.sort();

  for (const 도난당한학생 of lost) {
    if (reserve.includes(도난당한학생)) {
      // 여분있는데 도난당한학생은 여분이 없는거와 마찬가지므로 여분있는학생 명단에서 필터링 처리
      reserve = reserve.filter(여분있는학생 => 여분있는학생 !== 도난당한학생);
      체육복있는학생수++; // 도난당했으나 여분이 있었으므로 체육복 있는 학생 수에 더해줌.
    } else {
      체육복진짜없는학생들.push(도난당한학생);
    }
  }
  for (const 체육복진짜없는학생 of 체육복진짜없는학생들) {
    const 체육복진짜없는학생_앞번호 = 체육복진짜없는학생 - 1;
    const 체육복진짜없는학생_뒷번호 = 체육복진짜없는학생 + 1;
    if (reserve.includes(체육복진짜없는학생_앞번호)) { // 앞번호 학생이 여분이 있는 경우
      // "이제 여분없어요" 처리
      reserve = reserve.filter(여분있는학생 => 여분있는학생 !== 체육복진짜없는학생_앞번호);
      체육복있는학생수++;
    } else if (reserve.includes(체육복진짜없는학생_뒷번호)) { // 뒷번호 학생이 여분이 있는 경우
      // "이제 여분없어요" 처리
      reserve = reserve.filter(여분있는학생 => 여분있는학생 !== 체육복진짜없는학생_뒷번호);
      체육복있는학생수++;
    }
  }
  return 체육복있는학생수;
}