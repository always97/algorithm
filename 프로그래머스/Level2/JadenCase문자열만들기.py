def solution(s):
    answer = []
    arr = s.split(' ');
    
    for i in arr :
        answer.append(i.capitalize())
    
    return ' '.join(answer)