n = int(input())

arr = [ i for i in range(1,n+1)]

result = []

while len(arr) != 1 :
  result.append(arr.pop(0)) 
  arr.append(arr.pop(0))

result.append(arr[0])

print(" ".join(map(str, result)))