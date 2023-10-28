t = int(input())

def fix(now,replace,idx) :
  temp = now
  temp = temp[:idx] + replace * (len(temp) - idx)
  return temp

for i in range(1,t+1) :
  count = 0
  pre = input()
  now = '0'*len(pre)

  for j in range(len(now)) :
    if now[j] == pre[j] :
      continue
    count +=1
    now = fix(now,pre[j],j)



  print(f'#{i} {count}')