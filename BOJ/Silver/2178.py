n,m = map(int,input().split())

board = []
for _ in range(n) :
  board.append(list(map(int,input())))

# 우 상 좌 하
dx = [1,0,-1,0] 
dy = [0,1,0,-1]

q = []
q.append([0,0])

while(q) :
  x,y = q.pop(0)
  for i in range(4) :
    nx = dx[i] + x
    ny = dy[i]+ y
    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 :
      board[nx][ny] = board[x][y] + 1
      q.append([nx,ny]) 
  
print(board[n-1][m-1])
      