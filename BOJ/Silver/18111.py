import sys

N,M,B = map(int,sys.stdin.readline().split())

ground = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

answer = sys.maxsize
idx = 0

for floor in range(257) :
  초과분, 부족분 = 0,0

  for i in range(N) :
    for j in range(M) :
      if ground[i][j] > floor :
        초과분 += ground[i][j] - floor
      else :
        부족분 += floor - ground[i][j]
  
  if 초과분 + B >= 부족분 :
    if (초과분*2) + 부족분 <= answer :
      answer = (초과분*2) + 부족분
      idx = floor

print(answer, idx)