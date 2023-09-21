tc = int(input())

def myTurn(arr) :
  first_element = arr[0][0];
  found = False;
  for element in arr:
      if element[0] > first_element:
          found = True;
          break
      
  return found


for i in range(tc) :
  n,now = map(int,input().split());
  priority = list(map(int,input().split()));

  pr_arr = [(value, index) for index, value in enumerate(priority)]
  count = 0;
  index = 0;
  while(len(pr_arr)) :
    if myTurn(pr_arr) :
      pr_arr.append(pr_arr.pop(0))
    else : 
      popItem = pr_arr.pop(0);
      count +=1
      if popItem[1] == now :
        print(count)     

