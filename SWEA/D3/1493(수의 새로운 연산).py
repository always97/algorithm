t = int(input())

n = 300

my_list =  [[0 for _ in range(n)] for _ in range(n)]

my_list[1][1] = 1

# 가중치 시작값
start_v = 2

for i in range(1,len(my_list)) :
  for j in range(2,len(my_list[i])) :
    my_list[j][i] = my_list[j-1][i] + (j-1)

for i in range(1,len(my_list)) :
  for j in range(2,len(my_list[i])) :
    my_list[i][j] = my_list[i][j-1] + (start_v+(j-2))
  start_v +=1


def findIdx(target) :
  find_idx = -1
  for i in range(len(my_list)) :
    for j in range(len(my_list[i])) :
      if my_list[i][j] == target :
        find_idx = [j,i]
        break
  return find_idx

for i in range(1,t+1) :
  answer = 0
  p,q = map(int,input().split())
  px,py = findIdx(p)
  qx,qy = findIdx(q)

  answer = my_list[py+qy][px+qx]

  print(f'#{i} {answer}')