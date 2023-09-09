n = int(input())
coor = [list(map(int,input().split())) for _ in range(n)]

coor.sort(key = lambda x:( x[1], x[0]))

for i in range(0,len(coor)) :
  print(f'{coor[i][0]} {coor[i][1]}')