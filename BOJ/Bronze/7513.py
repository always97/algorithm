tc = int(input())

for i in range(tc) :
  m = int(input())
  word = [input() for _ in range(m)]

  n = int(input())
  answer = []
  for j in range(n):
    hint = list(map(int,input().split()))
    ps = []
    for k in range(1,len(hint)):
      ps.append(word[hint[k]])
    answer.append(''.join(ps))
  print(f"Scenario #{i + 1}:")
  print('\n'.join(answer), end="\n\n")