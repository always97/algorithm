P,N = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
answer = 1;
for i in A:
  if P+i < 200:
    answer+=1
    P = P+i

print(answer)