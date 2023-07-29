import sys

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)

n = int(input())

if n :
  scores = [int(sys.stdin.readline().strip()) for _ in range(n)]
  scores.sort()

  del_num = my_round(n * 0.15)

  if del_num > 0 :
    print(my_round(sum(scores[del_num:-del_num]) / len(scores[del_num:-del_num])))
  else :
    print(my_round(sum(scores)/len(scores)))
else :
  print(0)