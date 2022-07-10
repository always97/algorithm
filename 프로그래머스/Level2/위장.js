function solution(clothes) {
  let answer = 1;
  const obj = {};
  clothes.map((cloth)=> {
      if(!obj[cloth[1]]) {
          obj[cloth[1]] = [];
      }
      obj[cloth[1]].push(cloth[0]);
  })
  Object.entries(obj).map((v)=> {
      answer *= obj[v[0]].length+1;
  })
  
  return answer-1;
}