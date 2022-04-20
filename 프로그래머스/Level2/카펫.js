function solution(brown, yellow) {
  let answer = [];
  let total = brown+yellow;
  for(let height = 3; height<=(brown-2)/2; height++) {
      if(total % height === 0) {
          let width = total/height;
          if((height-2)*(width-2) === yellow) {
              answer = [height,width];
          }
      }
  }
  return answer;
}