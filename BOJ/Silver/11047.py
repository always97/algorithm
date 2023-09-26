n,k = map(int,input().split())

coin = []

for i in range(n) :
  coin.append(int(input()))
count = 0;
# 내림차순으로 만든다
coin.reverse()

for i in coin :
  if k <1 : break
  if i <= k :
    t = k//i;
    count += t
    k -= (t*i)

print(count)
