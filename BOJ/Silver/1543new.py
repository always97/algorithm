def find_word(word,  words, words_idx) :
  cur_idx = 0 
  target_idx = words_idx
  while cur_idx < len(word) :
    if target_idx >= len(words):
      return -1
    if word[cur_idx] == words[target_idx] :
      cur_idx += 1
      target_idx += 1
    else :
      return -1
  return target_idx

words = input()
target = input()


count = 0
char_idx = 0

while char_idx < len(words):
  # 남은 문자열이 target보다 짧은 경우
  if char_idx + len(target) > len(words): 
    break
  if target[0] == words[char_idx] :
    find_idx = find_word(target,words,char_idx)
    if find_idx != -1 :
      char_idx = find_idx
      count += 1
    else :
      char_idx +=1
  else :
    char_idx +=1

print(count)