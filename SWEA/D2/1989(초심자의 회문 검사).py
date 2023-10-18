t = int(input())

for i in range(1,t+1) :
  # 로직
  answer = 0
  data = input()

  print("---------")
  print(data)
  print(data[::-1])
  print("---------")

  if data == data[::-1] :
    answer = 1

  print(f'#{i} {answer}')
