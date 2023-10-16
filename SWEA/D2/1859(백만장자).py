n = int(input())

for i in range(1,n+1) :
  nn = int(input())
  data = list(map(int,input().split()))
  income = [];
  outcome = 0;

  for j in range(0,len(data)-1) :
    if j == len(data)-2 :
      if data[j] < data[j+1] :
        outcome += data[j+1]-data[j]
        if len(income) > 0 : # 구매한게 있다면
          for k in income :
            outcome += (data[j+1] - k) # 판매한 수익을 outcome에 더한다
          income = [] # 모두 판매하면 구매 리스트 초기화
    else :
      if data[j] <= data[j+1] :
        income.append(data[j])
      else :
        if len(income) > 0 : # 구매한게 있다면
          for k in income :
            outcome += (data[j] - k) # 판매한 수익을 outcome에 더한다
          income = [] # 모두 판매하면 구매 리스트 초기화

  print(f'#{i} {outcome}')
