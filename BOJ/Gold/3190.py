from collections import deque

N = int(input())
K = int(input())

EMPTY = 0
APPLE = 1
SNAKE = 2

board = [ [EMPTY] * N for _ in range(N) ]
# 사과 정보
for _ in range(K) :
  r,c = map(int,input().split())
  board[r-1][c-1] = APPLE

L = int(input())

dir_data = deque()
# 방향 정보
for _ in range(L) :
  time, dir = input().split()
  dir_data.append((int(time),dir))

time = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = 0
r, c = 0, 0
board[r][c] = SNAKE
snake_pos = deque()
snake_pos.append((r,c))
while time < N*N :
  time+=1
  nr, nc = r + dr[dir], c + dc[dir]
  # 벽 충돌 or 자기 자신 충돌
  if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == SNAKE:
    break
  r, c = nr, nc
  #사과일떄 처리
  if board[nr][nc] == APPLE :
    board[nr][nc] = SNAKE
    snake_pos.append((nr,nc))
  # 빈공간 처리 
  elif board[nr][nc] == EMPTY : 
    board[nr][nc] = SNAKE
    snake_pos.append((nr,nc))
    ddr, ddc = snake_pos.popleft()
    board[ddr][ddc] = EMPTY

  # 방향전환
  if dir_data and time == dir_data[0][0]:
    _, d = dir_data.popleft()
    if d == 'D':
        dir = (dir + 1) % 4
    else:  # 'L'
        dir = (dir - 1) % 4
print(time)