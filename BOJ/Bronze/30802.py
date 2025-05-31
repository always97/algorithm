import math
N = int(input())

sizes = list(map(int,input().split()))

T, P = map(int,input().split())

answer_t = 0
answer_p = 0
answer_p1 = 0

for num in sizes:
  answer_t += math.ceil(num/T)

answer_p = N//P 
answer_p1 = N%P

print(answer_t)
print(f"{answer_p} {answer_p1}")
