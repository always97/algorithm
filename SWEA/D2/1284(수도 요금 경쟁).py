n = int(input())

for i in range(1,n+1) :
  # a 는 1리터당 P 원
  # b 는 기본 요금이 Q , 월간 사용량 R 이하인 경우 기본만
  # 초과하면 초과량에 대해서 1리터당 S 원
  # 사용량 W
  P, Q, R, S, W = map(int,input().split())
  aPrice = P * W
  bPrice = Q

  if W > R :
    # 기본요금을 넘으면 초과량을더한다 
    bPrice += (W-R) * S

  print(f'#{i} {min(aPrice,bPrice)}')