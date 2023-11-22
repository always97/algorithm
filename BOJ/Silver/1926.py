
def bfs(x,y) :
  # 방문처리
  a[x][y] = 0
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  w = 1
  q = []
  q.append([x,y])

  while q :
    x,y  = q.pop(0)
    for i in range(4) :
      nx = dx[i] + x
      ny = dy[i]+ y
      if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1 :
        q.append([nx,ny]) 
        # 방문처리
        a[nx][ny] = 0
        w += 1


  return w

n,m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)] 

difV = 0
maxV = 0

for i in range(n) :
  for j in range(m) :
    if a[i][j] == 1 :
      difV += 1
      maxV = max(bfs(i,j), maxV)

print(difV)
print(maxV)