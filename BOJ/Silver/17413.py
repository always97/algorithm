S = input()

answer = []
stack = []
tag_mode = False

for char in S :
  if char == '<' :
    while stack:
      answer.append(stack.pop())
    tag_mode = True
    answer.append(char)
  elif char == '>' :
    tag_mode = False
    answer.append(char)
  elif tag_mode: 
    answer.append(char)
  else :
    if char == ' ':
      while stack:
        answer.append(stack.pop())
      answer.append(char)
    else :
      stack.append(char)

while stack :
  answer.append(stack.pop())

print(''.join(answer))