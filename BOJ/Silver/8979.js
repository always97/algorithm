const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [tc,...arr] = input;

const [N,K] = tc.split(' ').map(Number);

let countrys = [];

for(let i = 0; i<arr.length; i++) {
  const [idx, gold, silver, bronze] = arr[i].split(' ').map(Number);

  countrys.push({idx,gold,silver,bronze});

}

console.log(countrys);

countrys.sort((a,b)=> {
  if(a.gold > b.gold) {
    return 1;
  }
})

console.log(countrys);

function compare_medal(a,b) {
  if(a.gold < b.gold) {
    return 1;
  }else if(a.gold > b.gold) {
    return -1;
  }else {
    if(a.silver < b.silver) {
      return 1
    }else if(a.silver > b.silver) {
      return -1;
    }else {
      if(a.bronze < b.bronze) {
        return 1
      }else if(a.bronze > b.bronze) {
        return -1;
      }
    }
  }
}

countrys.sort(compare_medal);
console.log(countrys)