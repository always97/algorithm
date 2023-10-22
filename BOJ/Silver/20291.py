n = int(input())

my_dict = {}

for i in range(n) :
  s = input().split('.')[1]
  
  if s in my_dict :
    my_dict[s] +=1
  else :
    my_dict[s] = 1

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))


for key, value in sorted_dict.items() :
  print(f'{key} {value}')