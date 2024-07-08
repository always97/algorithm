function solution(n, m, section) {
  let answer = 0;

  let start_point = 0;
  for (let i = 0; i < section.length; i++) {
    if (section[i] <= start_point) continue;
    let paintingSection = section[i] + m - 1;
    if (paintingSection >= section[section.length - 1]) {
      answer++;
      break;
    } else {
      answer++;
      start_point = paintingSection;
    }
  }

  return answer;
}
