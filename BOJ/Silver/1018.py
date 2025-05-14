N,M = map(int,input().split())

board = [ input() for _ in range(N)]


def repaint_count(x,y) :
  # 시작 체크판 색깔
  countW = 0
  countB = 0

  for i in range(8):
    for j in range(8):
      cur = board[x+i][y+j]
      if (i+j)%2 == 0:
        if cur != 'W' : countW += 1 
        if cur != 'B' : countB += 1
      else:
        if cur != 'B' : countW += 1 
        if cur != 'W' : countB += 1
  
  return min(countW, countB)

min_change = float('inf')

for i in range(N - 7) :
  for j in range(M - 7):
    min_change= min(min_change, repaint_count(i,j))

print(min_change)