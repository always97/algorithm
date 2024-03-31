n = int(input())
arr = list(map(int,input().split()))

high_dragon = 0
answer = []
for i in arr :
  if i > high_dragon :
    high_dragon = i
    now_kill = 0
  else :
    now_kill +=1
    answer.append(now_kill)

print(max(answer))