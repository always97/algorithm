t = int(input())

for i in range(1,t+1) :
  # 로직
  answer = 0
  data = input()
  
  if data == data[::-1] :
    answer = 1

  print(f'#{i} {answer}')
