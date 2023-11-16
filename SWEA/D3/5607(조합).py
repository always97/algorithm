t = int(input())

for i in range(1,t+1) :
  answer= 0
  N,R = map(int,input().split())
  a = 1
  b = 1
  for i in range(R) :
    a*=(N-i)
    b*=(R-i)
  answer = (a/b)%1234567891

  print(f'#{i} {int(answer)}')