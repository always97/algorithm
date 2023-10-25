N,M = map(int,input().split())

arr = [i for i in range(1, N + 1)]

for i in range(M) :
  a,b = map(int,input().split())
  arr[a-1],arr[b-1] = arr[b-1],arr[a-1]


answer = ' '.join(map(str,arr))

print(answer)