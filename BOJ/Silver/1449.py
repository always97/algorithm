N, L = map(int,input().split())

water_pos = list(map(int,input().split()))

water_pos.sort()

cover_length = 0
count = 0
for i in water_pos:
  if i <= cover_length :
    continue
  count += 1
  cover_length = i+L -1

print(count)