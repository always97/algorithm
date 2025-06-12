isbn = input()

answer = 0
result = 0
memo_bonus = 0
for i in range(1, len(isbn)+1):
  bonus = 3 if i % 2 == 0 else 1
  if isbn[i-1].isdigit():
    result += bonus * int(isbn[i-1])
  else :
    memo_bonus = bonus

for i in range(1,10) :
  new_result = result + (memo_bonus * i)
  if new_result % 10 == 0:
    answer = i
    break

print(answer)