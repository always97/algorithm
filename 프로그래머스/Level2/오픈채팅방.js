function solution(record) {
  let answer = [];
  let user = new Map();
  
  record.map((data)=> {
      const [inout,id,nickname] = data.split(' ');
      if(inout === 'Enter' || inout === 'Change') { // 닉네임 설정
          if(inout === 'Enter') answer.push(`${id}님이 들어왔습니다.`)
          user.set(id,nickname);
      }else {
          answer.push(`${id}님이 나갔습니다.`)
      }
  });
  
  answer = answer.map((data)=> {
      let userId = data.split("님")[0];
      return data.replace(userId,user.get(userId));
  });
  return answer;
}