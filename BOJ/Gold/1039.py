N, K = input().split()
K = int(K)

from collections import deque

q = deque()
visited = set()
result = -1


q.append((N,0))
visited.add((N,0))

while q :
  cur_num, cur_k = q.popleft()

  if cur_k == K :
    result = max(result, int(cur_num))
    continue
  
  num_len = len(cur_num)
  for i in range(num_len-1):
    for j in range(i+1, num_len):
      num_list = list(cur_num)
      num_list[i],num_list[j] = num_list[j],num_list[i]
      
      next_num = ''.join(num_list)
      next_k = cur_k + 1

      if num_list[0] == '0' :
        continue
      if (next_num,next_k) not in visited:
        visited.add((next_num,next_k))
        q.append((next_num,next_k))

print(result)