from collections import deque
MAX_POS = 100000

def bfs(start, target):
  if start == target :
    return 0
  if start > target :
    return start-target
  
  q = deque()
  visited = [False] * (MAX_POS+1)
  # 큐로 관리할 상태는 현위치, 소요시간
  q.append((start,0))
  visited[start] = True

  while q :
    cur_pos, cur_time = q.popleft()
    move = [cur_pos+1 , cur_pos-1 , cur_pos * 2]

    for next_pos in move :
      if next_pos == target:
        return cur_time+1
      if 0<=next_pos<=MAX_POS and not visited[next_pos] :
        visited[next_pos] = True
        q.append((next_pos,cur_time+1))
  return -1


N, K = map(int,input().split())
result = bfs(N,K)
print(result)