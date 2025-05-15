# 백준 10773 (제로)

K = int(input())

num_arr = [];

for i in range(K) :
  num = int(input())
  if i == 0 and num == 0 :
    pass
  # 0 입력시 가장 최근값 빼기
  if num == 0 :
    num_arr.pop()
    continue
  num_arr.append(num)
print(sum(num_arr))