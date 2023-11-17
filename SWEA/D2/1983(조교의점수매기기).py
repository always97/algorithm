n = int(input())

for i in range(1,n+1) :
  nn,target = map(int,input().split())
  score = []
  for j in range(1,nn+1) :
    sum_score = 0
    mid,end,mission = map(int,input().split())
    sum_score += mid * 0.35
    sum_score += end * 0.45
    sum_score += mission * 0.2

    score.append([j,sum_score])

  score.sort(key=lambda x:x[1],reverse=True)

  rank = 0

  for j in range(len(score)) :
    if score[j][0] == target :
      rank = j
      break

  rank = rank // (nn//10)

  score_rank = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
  

  print(f'#{i} {score_rank[rank]}')
