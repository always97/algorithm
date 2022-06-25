function getScore(bonus,current_score) {  
    if(bonus === 'S') {
        return Math.pow(current_score,1);
    }else if(bonus === "D") {
        return Math.pow(current_score,2);
    }else {
        return Math.pow(current_score,3);
    }
} 

function solution(dartResult) {
    let answer = 0;
    let before_score = 0;
    for(let i = 1; i<dartResult.length; i++) {
        if(dartResult[i] === '0') continue;
        let addScore, option_score = 0;
        if(dartResult[i] === 'S' || dartResult[i] === "D" || dartResult[i] === "T") {
            let current_score = dartResult[i-1];
            if(current_score === '0') current_score = dartResult[i-2] === '1' ? 10 : 0; 
            addScore = getScore(dartResult[i],current_score)
            if(dartResult[i+1] === '*' || dartResult[i+1] === '#') {
                if(dartResult[i+1] === '*') {
                    option_score = before_score*2 - before_score;
                    addScore = addScore*2 + option_score;
                }else {
                    addScore = -addScore;
                }
                ++i;
            }
        }
        ++i;
        before_score = addScore - option_score;
        answer += addScore;
    }
    return answer;
}