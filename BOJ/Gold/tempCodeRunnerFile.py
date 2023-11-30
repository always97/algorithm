R,C = map(int,input().split())

board = []
hdist = [[-1 for _ in range(1002)] for _ in range(1002)]
fdist = [[-1 for _ in range(1002)] for _ in range(1002)]

for _ in range(R) :
  board.append(list(input()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
q1= []
q2= []

for i in range(R) :
  for j in range(C) :
    if board[i][j] == 'J' :
      q1.append([i,j])
      hdist[i][j] = 0
    if board[i][j] == 'F' :
      q2.append([i,j])
      fdist[i][j] = 0

# 불 
while q2 : 
  x,y = q2.pop(0)
  for dir in range(4) :
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0>nx or nx>=R or 0>ny or ny>=C : continue
    if board[nx][ny] == '#' or fdist[nx][ny] >=0 : continue
    fdist[nx][ny] = fdist[x][y] +1
    q2.append([nx,ny])

# 지훈
while q1 : 
  x,y = q1.pop(0)
  for dir in range(4) :
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0>nx or nx>=R or 0>ny or ny>=C : 
      print(hdist[x][y]+1)
    if fdist[nx][ny] >= 0 or board[nx][ny] == '#' : continue
    if hdist[nx][ny] != -1 and fdist[nx][ny] <= hdist[x][y]+1 : continue
    hdist[nx][ny] = hdist[x][y] +1
    q1.append([nx,ny])

print("IMPOSSIBLE")