n = int(input())

for i in range(1,n+1) :
  startNum = input()
  seeNum = set()
  idx = 1
  while len(seeNum) < 10 :
    nowNum = str(int(startNum) * idx)
    for see in nowNum :
      seeNum.add(see)
    idx +=1
  print(f'#{i} {nowNum}')