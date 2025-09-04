N, M = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0

while start <= end :
  total = 0
  mid = (start+end) // 2

  for tree_h in trees:
    if tree_h > mid :
      total += tree_h - mid
  if total >= M:
    result = mid
    start = mid + 1
  else :
    end = mid - 1

print(result)