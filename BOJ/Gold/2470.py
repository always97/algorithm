N = int(input())

sol_arr = list(map(int,input().split()))
sol_arr.sort()

start = 0
end = N-1
min_val = float('inf')
best_pair = (0,0)

while start < end:
  cur_sum = sol_arr[start]+sol_arr[end]
  if abs(cur_sum) < abs(min_val) :
    min_val = cur_sum
    best_pair = (sol_arr[start], sol_arr[end])
  
  if cur_sum == 0 :
    break
  elif cur_sum > 0 : 
    end -= 1
  else :
    start += 1

print(best_pair[0], best_pair[1])