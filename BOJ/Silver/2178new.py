from collections import deque

N, M = map(int,(input().split()))

board = [list(map(int,input())) for _ in range(N)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()
q.append((0,0))

while(q):
  r, c = q.popleft()
  for i in range(4):
    nr, nc = r + dr[i], c + dc[i]
    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1:
        board[nr][nc] = board[r][c] +1
        q.append((nr,nc))

print(board[N-1][M-1])