n = int(input())

arr = list(int(input()) for _ in range(n))

able = True
stack = []
start = 1
answer = []

for i in arr :
  while start <= i :
    stack.append(start)
    answer.append('+')
    start +=1
  if stack[-1] == i :
    stack.pop()
    answer.append('-')
  else : able = False

if not able :
  print("NO")
else :
  for i in answer :
    print(i)