def solution(food):
    answer = ''
    pre = ''
    for idx in range(1,len(food)) :
        for j in range(food[idx]//2) :
            pre+=str(idx)
    answer+=(pre+'0'+pre[::-1])
    return answer