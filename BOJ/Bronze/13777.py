while True:
  n = int(input())
  if n == 0:
    break

  low = 1
  high = 50
  result = []

  while True:
    mid = (low + high) // 2
    result.append(mid)
    if mid == n:
      break
    elif n < mid : 
      high = mid - 1
    else :
      low = mid + 1

  print(' '.join(map(str,result)))