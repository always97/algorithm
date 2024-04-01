n = int(input())

arr = list(map(int,input().split()))

s,e = arr[0],arr[0]
ans = 0

for i in range(1,n) :
  if e >= arr[i] :
    s = arr[i]
    e = arr[i]
  else :
    e = arr[i]
  ans = max(ans,e-s) 

print(ans)



