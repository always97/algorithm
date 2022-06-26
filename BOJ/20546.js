const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

let s = input[0];
let t = input[1].split(' ');

s = parseInt(s);
t = t.map((num)=> parseInt(num));


const answer = solution(s, t);

function solution(s, t) {
    let a =0, b =0, aRest = s, bRest = s;
    let downStack = 0, upStack = 0, bFlag = false , bBuyIdx;

    for(let i =0; i<t.length; i++) {
        if(i>0) {
            if(t[i-1]>t[i]) {
                downStack++;
                upStack = 0;
            }else if(t[i-1]<t[i]){
                upStack++;
                downStack = 0;
            }
        }
        if(t[i] <= aRest) {
            a = Math.floor(aRest/t[i]);
            aRest = aRest- a *t[i];
        }
        if(downStack >= 3) {    
            if(t[i] <= bRest) {
                let tmpB = Math.floor(bRest/t[i]);
                bBuyIdx = i;
                b = b+tmpB;
                bRest = bRest- tmpB*t[i];            
            }
        }
        if(upStack >=3) {
            if(!bFlag && i>bBuyIdx) {
                bFlag = true;
                b = b*t[i] + bRest;
            }
        }
    }

    a = a*t[t.length-1] + aRest;
    if(!bFlag) b = b*t[t.length-1] + bRest;
    
    if(a>b) {
        return "BNP";
    }else if(b>a) {
        return "TIMING";
    }else return "SAMESAME";
}

console.log(answer);