n = int(input())

switch_arr = list(map(int,input().split()))

student_num = int(input())

def switch_state(gender, number, switches):
  switch_count = len(switches)
  # 남학생인 경우
  if gender == 1:
    change_num = number
    while change_num <= switch_count :
      idx_to_change = change_num - 1
      switches[idx_to_change] = 1 - switches[idx_to_change]
      change_num += number
  # 여학생인 경우
  elif gender == 2 :
    center_idx = number - 1
    switches[center_idx] = 1 - switches[center_idx]
    offset = 1
    while True:
      left_idx = center_idx - offset
      right_idx = center_idx + offset
      if left_idx < 0 or right_idx >= switch_count:
        break
      if switches[left_idx] == switches[right_idx]:
        switches[left_idx] = 1 - switches[left_idx]
        switches[right_idx] = 1 - switches[right_idx]
        offset += 1
      else: 
        break

for _ in range(student_num):
  gender, switch_num = map(int,input().split())
  switch_state(gender,switch_num, switch_arr)

for i in range(n):
  print(switch_arr[i], end=" ")
  if (i+1)%20 == 0:
    print()