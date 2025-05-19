from collections import defaultdict

N, K = map(int,input().split())

num_arr = list(map(int,input().split()))

start = 0
result = 0
counter = defaultdict(int)

for end in range(N): 
  cur_num = num_arr[end]
  counter[cur_num] += 1

  while counter[cur_num] > K :
    start_num = num_arr[start]
    counter[start_num] -= 1
    start += 1
    
  result = max(result, end-start +1 )

print(result)