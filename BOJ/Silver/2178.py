n,m = map(int,input().split())

dist = [[-1] for _ in range(n+1)]

board = []

for i in range(n) :
  input_str = input()
  board.append([int(j) for j in (input_str)])

# 우 상 좌 하
dx = [1,0,-1,0] 
dy = [0,1,0,-1]

q = []
q.append([0,0])
dist[0][0] = 0

while(q) :
  x,y = q.pop()
  for i in range(4) :
    nx = dx[i] + x
    ny = dy[i]+ y
    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 :
        # 방문처리
      dist[nx][ny] = dist[x][y] + 1
      board[nx][ny] = 1
      # board[nx][ny] = 0
      q.append([nx,ny]) 
  
print(dist[n-1][m-1]+1)
      