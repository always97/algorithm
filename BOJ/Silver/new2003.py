N, M = map(int,input().split())
num_arr = list(map(int,input().split()))

from collections import deque

window = deque()
cur_sum = 0
result = 0
for i in range(N):
  window.append(num_arr[i])
  cur_sum += num_arr[i]

  while cur_sum > M and window:
    cur_sum -= window.popleft()

  if cur_sum == M :
    result += 1
    cur_sum -= window.popleft()


print(result)

# 인덱스를 활용한 투 포인터 코드

N, M = map(int,input().split())
num_arr = list(map(int,input().split()))

cur_sum = 0
result = 0
start = 0

for end in range(N):
  cur_sum += num_arr[end]

  while cur_sum > M and start <= end :
    cur_sum -= num_arr[start]
    start +=1
  if cur_sum == M :
    result += 1
print(result)