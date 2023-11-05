
for _ in range(10) :
  n = int(input())
  arr = list(map(int,input().split()))
  signal = False
  start_n, end_n = 1 , 6
  while not signal :
    for i in range(start_n,end_n) :
      if arr[0] - i > 0 :
        item = arr.pop(0) - i
        arr.append(item)
      else :
        arr.pop(0)
        arr.append(0)
        signal = True
        break
  print(f'#{n} {" ".join(map(str,arr))}')
    