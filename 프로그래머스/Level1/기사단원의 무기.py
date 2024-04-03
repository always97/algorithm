import math

def count_divisors(num):
    count = 0
    sqrt_num = int(math.sqrt(num))
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            count += 2  # i와 num//i가 모두 약수이므로 count + 2
    # 만약 num이 제곱수라면, 위의 반복문에서 중복으로 더해지니까 -1
    if sqrt_num * sqrt_num == num:
        count -= 1
    return count

def solution(number, limit, power):
    answer = 0
    
    for i in range(1,number+1) :
        if count_divisors(i) > limit :
            answer += power
        else :
            answer += count_divisors(i)

    return answer