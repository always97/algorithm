def time_to_sec(time):
  m,s = map(int,time.split(':'))
  return m * 60 + s
def sec_to_time(sec):
  m = sec//60
  s = sec%60
  return f"{m:02}:{s:02}"

N = int(input())
GAME_TIME = 48*60
goals = []
for _ in range(N):
  team, time = input().split()
  team = int(team)
  goals.append((team,time_to_sec(time)))

t1_point = 0
t2_point = 0
t1_win_sec = 0
t2_win_sec = 0
last_event_sec = 0

for goal_data in goals:
  cur_sec = goal_data[1]

  interver_sec = cur_sec - last_event_sec

  if t1_point > t2_point :
    t1_win_sec += interver_sec
  elif t2_point > t1_point:
    t2_win_sec += interver_sec
  
  if goal_data[0] == 1 :
    t1_point += 1
  else : 
    t2_point += 1

  last_event_sec = cur_sec

last_interval_time = GAME_TIME - last_event_sec

if t1_point > t2_point :
  t1_win_sec += last_interval_time
elif t2_point > t1_point :
  t2_win_sec += last_interval_time

print(sec_to_time(t1_win_sec))
print(sec_to_time(t2_win_sec))



