def find_lds(word):
  n = len(word)
  if n == 0:
    return ""
  lds = word[-1]

  for i in range(n-2, -1, -1) :
    if word[i] > lds[-1]:
      lds += word[i]
    else :
      break;
  return lds
n = int(input())
for i in range(n):
  word = input();
  print(f"{word}의 가장 긴 감소 접미사는 {find_lds(word)}입니다.")