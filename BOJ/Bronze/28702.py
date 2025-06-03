inputs = [input() for _ in range(3)]

now = 0

for k in inputs:
  if k.isdigit():
    now = int(k)
  else :
    now += 1


target = now + 1 

if target%3 == 0 and target % 5 == 0:
  print('FizzBuzz')
elif target%3==0:
  print('Fizz')
elif target%5==0:
  print('Buzz')
else :
  print(str(target))