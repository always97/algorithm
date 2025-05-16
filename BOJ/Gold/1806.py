N, S = map(int,input().split())

arr = list(map(int,input().split()))

start = 0
end = 0
cur_sum = 0
result = N+1

while end < N :
  cur_sum += arr[end]
  while cur_sum >= S and start <= end:
    result = min(result, end-start+1)
    cur_sum -= arr[start]
    start += 1
  end += 1

print(result) if result < N+1 else print(0)