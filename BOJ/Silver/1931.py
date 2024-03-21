n = int(input())

timeArr = []

for _ in range(n) :
  s,e = map(int,input().split)
  timeArr.append([s,e])

timeArr.sort(lambda x: (x[1],x[0]))

ans = end = 0

for fs,fe in timeArr :
  if end <= fs :
    ans+=1
    end = fe

print(ans)