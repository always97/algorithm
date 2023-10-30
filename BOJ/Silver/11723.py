n = int(input())

arr = set()

for i in range(n) :
  com_input = input().split()

  if len(com_input) == 1 :
    control = com_input[0]
    num = 0
  elif len(com_input) == 2 :
    control, num = com_input


  if control=='add' :
    arr.add(int(num))
  elif control == 'check' :
    if int(num) in arr :
      print(1)
    else : print(0)
  elif control == 'remove' :
    arr.remove(int(num))
  elif control == 'toggle' :
    if int(num) in arr :
      arr.remove(int(num))
    else :
      arr.add(int(num))
  elif control == 'all' :
    arr = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
  else :
    arr = set()