def getMaxKey(cmap,aKey,bKey) :
    if cmap[aKey] == cmap[bKey] :
        if (aKey) < (bKey):
            return aKey
        else :
            return bKey
    return aKey if cmap[aKey] > cmap[bKey] else bKey

def solution(survey, choices):
    answer = ''
    # 1~3 비동의 4 모름 5~7 동의
    # 비동의시 survey[0]
    # 동의시 survey[1]
    cmap = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    group = [['R','T'],['C','F'],['J','M'],['A','N']]
    for i in range(len(choices)) :
        disagree, agree = survey[i]
        if choices[i] < 4 : # 비동의 쪽
            score = 4-choices[i]
            cmap[disagree]+=score
        elif choices[i] > 4: #동의 쪽
            score = choices[i]-4
            cmap[agree]+=score
    for a,b in group :
        answer += getMaxKey(cmap,a,b)

    return answer