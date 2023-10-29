t = int(input())

for i in range(1,t+1) :
  answer= 0
  n = int(input())
  my_arr = []
  for j in range(n) :
    line = input()
    line_arr = [int(digit) for digit in str(line)]
    my_arr.append(line_arr)
  for k in range(n) :
    answer += my_arr[k][n//2]
    if k <= n//2 :
      for h in range(k) :
        answer += my_arr[k][(n//2)+h+1]
        answer += my_arr[k][(n//2)-h-1]
    else :
      for h in range((n-1)-k) :
        answer += my_arr[k][(n//2)+h+1]
        answer += my_arr[k][(n//2)-h-1]
  print(f'#{i} {answer}')