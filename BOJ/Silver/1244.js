// 스위치 켜고 끄기

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

let switchNum = Number(input[0]);
let state = input[1].split(' ');
let studentNum = Number(input[2]);
let studentInfo = [];

for(let i = 3; i<3+studentNum; i++) {
    let [gender , have] = input[i].split(' ');
    studentInfo.push({gender,have});
}


for(let i = 0; i<studentNum; i++) {
    let cur_student_gender = parseInt(studentInfo[i].gender);
    let cur_student_have = parseInt(studentInfo[i].have);
    if(cur_student_gender === 1) {
        for(let j = 0; j<switchNum; j++) { // 남학생
            if((j+1)%cur_student_have === 0) { // 스위치 번호가 자기가 받은 수의 배수인 경우   
                state[j] = parseInt(state[j]) === 0 ? 1 : 0; // 상태 변경 
            }
        }
    }else {
        changeState(cur_student_have-1);
    }
} 


function changeState(have) {    // 여학생의 경우
    let startIdx = have;
    let lastIdx = have;
    for(let i = 1; i<switchNum/2; i++) {
        if(parseInt(state[have-i]) == parseInt(state[have+i])) {
            if(have-i < startIdx) {
                startIdx = have-i;
                lastIdx = have+i;
            }
        }
    } 
    if(startIdx == have) {
        state[have] = parseInt(state[have]) == 0 ? 1 : 0;
    }else {
        for(let i = startIdx; i<=lastIdx; i++) {
            state[i] = parseInt(state[i]) == 0 ? 1 : 0;
        }
    }
}
let answer = '';
let tmpArr = [];
let count = 0;
if(state.length> 20) {
    for(let i = 0; i<state.length/20+1; i++) {
        let arr = state.splice(count,20*(i+1));
        count += (20*i);
        tmpArr.push(arr);
    }
}else {
    answer = state.join(' ');
}
if(tmpArr) {
    for(let i = 0; i<tmpArr.length; i++) {
        answer += tmpArr[i].join(' ');
        answer += "\n";
    }
}

console.log(answer);