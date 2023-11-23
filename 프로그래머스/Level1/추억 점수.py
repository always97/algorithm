def solution(name, yearning, photo):
    answer = []
    scores = {}
    for i in range(len(yearning)) :
        scores[name[i]] = yearning[i]
    
    for i in range(len(photo)) :
        temp = []
        for j in range(len(photo[i])) :
            if photo[i][j] in name :
                temp.append(scores.get(photo[i][j]))
        answer.append(sum(temp))
    return answer