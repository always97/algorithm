N = int(input())

board = [list(map(int,input())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

result = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c) :
  visited[r][c] = True
  count = 1
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0<=nr<N and 0<=nc<N:
      # 방문하지 않은 집
      if not visited[nr][nc] and board[nr][nc] == 1:
        count += dfs(nr, nc)
  return count

for i in range(N):
  for j in range(N):
    if board[i][j] == 1 and not visited[i][j]:
      # 1 이면 집 이므로 탐색 dfs 시작
      house_count = dfs(i,j)
      result.append(house_count)

print(len(result))
result.sort()

for count in result:
  print(count)
      
