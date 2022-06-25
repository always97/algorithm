function getBinary(num,k){
    return num.toString(2).length <k ? num.toString(2).padStart(k,"0") : num.toString(2);
}

function solution(n, arr1, arr2) {
    var answer = [];
    let map1,map2;
    for(let i =0; i<n; i++) {
        map1 = getBinary(arr1[i],n);
        map2 = getBinary(arr2[i],n);
        let map = '';
        for(let j=0; j<n; j++) {
            if(map1[j] === '0' && map2[j] === '0') {
                map += ' ';
            }else map += "#"
        }
        answer.push(map);
    }
    return answer;
}