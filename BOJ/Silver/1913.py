N = int(input())
target = int(input())

board = [[0] * N for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

r,c = 0, 0
num = N*N
direction = 0

board[r][c] = num
target_r, target_c = 0, 0

if num == target:
    target_r, target_c = r + 1, c + 1

while num > 1 :
  num -= 1

  nr = r + dr[direction] 
  nc = c + dc[direction] 
  # 범위 벗어난 경우
  if not (0<=nr<N and 0<=nc<N and board[nr][nc] == 0) :
    direction = (direction+1) % 4
    nr = r + dr[direction] 
    nc = c + dc[direction] 
  if num == target:
    target_r, target_c = nr+1, nc+1
  board[nr][nc] = num
  r,c = nr, nc


for i in range(N):
  print(' '.join(map(str, board[i])))

print(f"{target_r} {target_c}")