my_map = [list(map(int, input().split())) for _ in range(5)]
answer_map = [list(map(int, input().split())) for _ in range(5)]

check_map = [ [0]*5 for _ in range(5)]

is_bingo = False

def find_idx(x,map) :
  for i in range(5) :
    for j in range(5) :
      if map[i][j] == x :
        return [i,j]
      
def bingoCheck(map) :
  bingo = check_row(map) + check_col(map) + check_cross(map)
  if bingo >=3 : return True
  return False

def check_row(map) :
  res = 0
  for i in range(5):
    if map[i][0] == 1 :
      cnt = (map[i][1]+map[i][2]+map[i][3]+map[i][4])
      if cnt == 4:
        res += 1
  return res

def check_col(map) :
  res = 0
  for i in range(5):
    if map[0][i] == 1:
      cnt = (map[1][i]+map[2][i]+map[3][i]+map[4][i])
      if cnt == 4:
        res += 1
  return res

def check_cross(map) :
  res = 0
  if map[0][0] == 1 :
    cnt = (map[1][1]+map[2][2]+map[3][3]+map[4][4])
    if cnt == 4 : res +=1
  if map[0][4] == 1 :
    cnt2 = (map[1][3]+map[2][2]+map[3][1]+map[4][0])
    if cnt2 == 4 : res +=1
  return res


for i in range(5) :
  for j in range(5) :  
    x,y = find_idx(answer_map[i][j],my_map)
    check_map[x][y] = 1
    if bingoCheck(check_map) :
      print((5*i) + (j+1))
      is_bingo = True
      break
  if is_bingo :
    break