n = int(input())

for i in range(1,n+1) :
  nn = int(input())
  data = list(map(int,input().split()))

  sellPrice = 0;
  outcome = 0;

  for v in data[::-1] :
    if v >= sellPrice: 
      sellPrice = v
    else :
      outcome += sellPrice - v

  print(f'#{i} {outcome}')
