ch, cm = map(int,input().split())

cost = int(input())

nm = cm+cost
nh = ch
if nm > 59 :
  nm-=60
  nh +=1

  if nh > 23 :
    nh -= 24

print(f'{nh} {nm}')