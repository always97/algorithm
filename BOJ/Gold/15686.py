# 거리 구하는 함수
def getDistance(home,store) :
  return abs(home[0]-store[0]) + abs(home[1]-store[1])

def dfs(cur,arr) :
  global answer

  if len(arr) == M :
    result = 0

    for home in homes :
      min_dst = float("inf")
      for store in arr :
        dist = getDistance(home,store)
        min_dst = min(dist, min_dst)      
      result += min_dst
    
    answer = min (answer , result)
    return 
  
  if cur == len(stores):
    return
  
  # 선택한 경우
  dfs(cur+1, arr+[stores[cur]])
  # 선택하지 않은 경우
  dfs(cur+1, arr)
  
  

N,M = map(int,input().split())

cityMap = [list(map(int,input().split())) for _ in range(N)]
answer=float('inf')
homes = []
stores = []


# 집과 치킨집 좌표 저장
for i in range(N):
  for j in range(N):
    if cityMap[i][j] == 1 :
      homes.append([i+1,j+1])
    elif cityMap[i][j] == 2 :
      stores.append([i+1,j+1])

dfs(0,[])
print(answer)

