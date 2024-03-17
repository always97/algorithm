K,N = map(int,input().split()) 
lis = [int(input()) for _ in range(K)]  

start =1
end = max(lis)

while start <= end :
  mid = (start+end)//2
  count = 0
  for i in lis :
    count += i//mid
  
  if count >= N :
    start = mid+1
  else :
    end = mid-1

print(end)

