def isGroup(word) :
  visit = set(word[0])
  for i in range(1, len(word)) :
    # 처음 발견한 단어이면 저장
    if word[i] not in visit: visit.add(word[i])
    #이미 존재하는 단어이면서 이전 단어와 다르면 false 리턴
    elif word[i] != word[i-1]: return False
  return True

N = int(input())

word_list = [ input() for _ in range(N)]

result = 0
for i in range(N) :
  if isGroup(word_list[i]): result += 1

print(result)