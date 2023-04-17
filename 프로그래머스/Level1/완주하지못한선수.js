function solution(participant, completion) {
    var answer = '';
    participant.sort();
    completion.sort();
    for(var i in participant) {
        if(participant[i] !== completion[i]) {
            answer = participant[i];
            return answer;
        }
    }
    return answer;
}