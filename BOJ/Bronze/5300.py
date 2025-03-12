n = int(input())

result = []

for i in range(1, n+1) :
  result.append(str(i))
  if i % 6 == 0 or i == n:
    result.append("Go!")

print(' '.join(result))