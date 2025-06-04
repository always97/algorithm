from collections import deque
M, N = map(int, input().split())

board = [ list(map(int, input().split())) for _ in range(N) ]
dist = [[0]*M for _ in range(N)]
q = deque()

for i in range(N):
  for j in range(M) :
    if board[i][j] == 1 :
      q.append((i,j))
    elif board[i][j] == 0 :
      dist[i][j] = -1

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

while q :
  r, c = q.popleft()
  for dir in range(4):
    nr = r + dr[dir]
    nc = c + dc[dir]
    # 범위 벗어남
    if nr < 0 or nr >= N or nc < 0 or nc >= M: 
      continue
    if dist[nr][nc] >= 0 :
      continue
    dist[nr][nc] = dist[r][c] + 1
    q.append((nr,nc))


def get_answer():
  answer = 0
  for i in range(N):
    for j in range(M):
      if dist[i][j] == -1:
        return -1
      answer = max(answer, dist[i][j])
  return answer

answer = get_answer()
print(answer)