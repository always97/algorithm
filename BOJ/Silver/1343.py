txt = input().split('.')
answer = ""
for s in txt :
  if len(s) % 2 == 1 :
    print(-1)
    break
  if len(s)>=4 :
    answer+=(('AAAA')*(len(s)//4))
    if len(s)%4 != 0 :
      answer+="BB"
  elif len(s) == 2:
    answer+="BB"
  answer+='.'
else : 
  print(answer[:-1])

