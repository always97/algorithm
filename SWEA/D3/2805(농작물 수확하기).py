t = int(input())

for i in range(1,t+1) :
  answer= 0
  n = int(input())
  line = [list(map(int,input())) for _ in range(n)]
  mid = n//2
  for k in range(n) :
    if k <= mid :
      answer += sum(line[k][mid-k: mid+k+1])
    else :
      answer += sum(line[k][k-mid: mid-k])


  print(f'#{i} {answer}')