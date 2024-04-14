n , m = map(int,input().split())

arr = [ i for i in range(1,n+1)]

for i in range(m) :
  a,b = map(int,input().split())
  arr[a-1:b] = reversed(arr[a-1:b])

print(*arr)
