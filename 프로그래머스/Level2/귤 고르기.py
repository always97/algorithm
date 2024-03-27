def solution(k, tangerine):
    answer = 0
    countArr = {}
    
    for i in tangerine :
        if i in countArr :
            countArr[i] +=1
        else : countArr[i] = 1
    
    sortCountArr = sorted(countArr.items(),key=lambda x:x[1], reverse=True)
    
    for i in range(len(sortCountArr)) :
        k -= sortCountArr[i][1]
        answer +=1
        if k <= 0:
            break
    
    return answer