# 백준 10773 (제로)

K = int(input())

num_arr = []

for i in range(K) :
  num = int(input())
  # 0 입력시 가장 최근값 빼기
  if num == 0 : 
    if num_arr : num_arr.pop()
  else : num_arr.append(num)
print(sum(num_arr))