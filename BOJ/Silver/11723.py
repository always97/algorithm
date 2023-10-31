import sys

n = int(input())

arr = set()

for i in range(n) :
  com_input = sys.stdin.readline().strip().split()

  if len(com_input) == 1 :
    if com_input[0] == 'all' :
      arr = set([i for i in range(1,21)])
    else :
      arr = set()
  else :
    control, num = com_input
    num = int(num)

    if control=='add' :
      arr.add(num)
    elif control == 'remove' :
      arr.discard(num)
    elif control == 'check' :
      if num in arr :
        print(1)
      else : print(0)
    elif control == 'toggle' :
      if num in arr :
        arr.discard(num)
      else :
        arr.add(num)
