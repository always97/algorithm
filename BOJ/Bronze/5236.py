def find_lds(word):
  n = len(word)
  if n == 0:
    return ""
  lds = word[-1]

  for i in range(n-2, -1, -1) :
    if word[i] > lds[0]:
      lds = word[i] + lds
    else :
      break;
  return lds
n = int(input())
for i in range(n):
  word = input().strip();
  print(f"The longest decreasing suffix of {word} is {find_lds(word)}")