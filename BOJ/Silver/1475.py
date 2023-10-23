n = input()

mySet = [0,1,2,3,4,5,6,7,8,9]
count = 1

def solution(mySet,number) :
  global count

  if number == 6:
    other_number = 9
  elif number == 9:
    other_number = 6
  else : 
    other_number = number
  if other_number in mySet:
    mySet.remove(other_number)
  else:
    count +=1
    newSet= [0,1,2,3,4,5,6,7,8,9]
    mySet.extend(newSet)
    mySet.remove(int(n[i]))


for i in range(len(n)) :
  if int(n[i]) in mySet :
    mySet.remove(int(n[i]))
  else :
    solution(mySet,int(n[i]))


print(count)