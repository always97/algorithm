N, M = map(int,input().split())

arr = [int(input()) for _ in range(N)]
arr.sort()

start = 0
end = 0
result = float('inf')


while end < N and start <= end :
  cur_diff = arr[end] - arr[start]
  # 목표 차이보다 부족하면 차이를 키워야함
  if cur_diff < M:
    end += 1
  # 목표차이 만족시 갱신후 차이를 좁혀본다.
  else : 
    result = min(result,cur_diff)
    start += 1

print(result)
