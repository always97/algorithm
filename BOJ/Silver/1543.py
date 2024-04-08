sentence = input()
word = input()

count = 0
index = 0

while index < len(sentence) :
  found_index = sentence.find(word,index)
  if found_index == -1 :
    break
  else :
    count +=1 
    index = found_index+ len(word)

print(count)