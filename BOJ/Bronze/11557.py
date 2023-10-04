T = int(input())

for i in range(T) :
  n = int(input())
  schools = []
  for j in range(n) :
    school,beer = input().split()
    schools.append([school,int(beer)])
  schools.sort(key=lambda x:x[1],reverse=True)

  print(schools[0][0])