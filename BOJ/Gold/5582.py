a = input()
b = input()

n,m = len(a), len(b)

prev = [0] * (m+1)
curr = [0] * (m+1)
result = 0

for i in range(1, n+1) :
  for j in range(1, m+1) :
    if a[i-1] == b[j-1] :
      curr[j] = prev[j-1] +1
      result = max(result, curr[j])
    else :
      curr[j] = 0
  prev, curr = curr, [0] * (m+1)

print(result)