N = int(input())

dist_arr = list(map(int,input().split()))
oil_arr = list(map(int,input().split()))

min_cost_oil = oil_arr[0]
result_cost = 0

for i in range(1,N):
  result_cost += min_cost_oil * dist_arr[i-1]
  min_cost_oil = min(min_cost_oil, oil_arr[i])

print(result_cost)