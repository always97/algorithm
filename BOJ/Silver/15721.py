import sys
def solve():
  A = int(sys.stdin.readline())
  T = int(sys.stdin.readline())
  target_num = int(sys.stdin.readline())

  bbun_count = 0
  degi_count = 0

  cur_people_idx = 0

  game_round = 0

  while True:

    cur_repeat = (game_round + 2)

    seq_arr = []

    seq_arr.append(0)
    seq_arr.append(1)
    seq_arr.append(0)
    seq_arr.append(1)

    for _ in range(cur_repeat):
      seq_arr.append(0)
    for _ in range(cur_repeat):
      seq_arr.append(1)

    for cur_target in seq_arr:
      if cur_target == 0 :
        bbun_count += 1
        if target_num == 0 and bbun_count == T:
          print(cur_people_idx)
          return
      else:
        degi_count += 1
        if target_num == 1 and degi_count == T:
          print(cur_people_idx)
          return
      cur_people_idx = (cur_people_idx + 1) % A
    
    game_round += 1


solve()