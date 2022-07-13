// 소가 길을 건너간 이유
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const n = input[0];
let cowRoad = new Map();
let answer = 0;

for(let i = 1; i <=n; i++) {
    const [cow,road] = input[i].split(' ');
    
    if(!cowRoad.get(cow)) {
        cowRoad.set(cow,road);
    }
    if (cowRoad.get(cow) !== road) {
        answer++;
        cowRoad.set(cow,road);
    }

    
}

console.log(answer);