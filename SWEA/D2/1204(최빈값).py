n = int(input())

for i in range(1,n+1) :
  nn = int(input())
  data = list(map(int,input().split()))
  arr = [0] *101

  for j in data :
    arr[j]+=1

  max_value = arr[0]
  max_index = 0
  for k in range(1, len(arr)):
    if arr[k] >= max_value:  # '>='를 사용하여 동일한 최댓값 처리
        max_value = arr[k]
        max_index = k
  
  print(f'#{nn} {max_index}')