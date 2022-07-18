function solution(n) {
    let answer = n;
    for(let i = 0; i<n; i++) {
        if(n%i === 1) {
            if(i<answer) answer = i;
        }
    }
    return answer;
}