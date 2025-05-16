n = int(input())

num_arr = list(map(int,input().split()))

x = int(input())

left = 0
right = n-1
result = 0

num_arr.sort()

while left < right :
  cur_num = num_arr[left] + num_arr[right]
  if cur_num == x :
    result += 1
    left += 1
    right -= 1
  elif cur_num > x :
    right -= 1
  elif cur_num < x :
    left += 1

print(result)
