N,M = map(int,input().split())

points = list(map(int,input().split()))

answer = 0
left = 0
right = 1

while right <= N and left <= right :
  total = sum(points[left:right])
  if total == M :
    answer +=1
    left+=1
    right = left+1
  if total < M:
    right+=1
  if total >M:
    left+=1
    right = left+1
    

print(answer)

# import sys

# n, m = map(int,sys.stdin.readline().split())
# array = list(map(int,sys.stdin.readline().split()))

# cnt = 0
# left = 0
# right = left + 1

# while right <= n and left <= right:
#   total = sum(array[left:right])
#   if total == m:
#     cnt += 1
#     left += 1
#     right = left + 1
#   if total < m:
#     right += 1
#   if total > m:
#     left += 1
#     right = left + 1

# print(cnt)