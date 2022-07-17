function solution(arr, divisor) {
    let answer = [];
    arr.map((v)=> {
        if(parseInt(v%divisor) == 0) {
            answer.push(v);
        }
    });
    if(!answer.length) answer.push(-1)
    return answer.sort((a,b)=> a-b);;
}