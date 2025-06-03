N = int(input())

stairs = [int(input()) for _ in range(N)]

dp = [0] * N

if N == 0:
  print(0)
elif N == 1:
  print(stairs[0])
elif N == 2:
  print(stairs[0] + stairs[1])
elif N == 3:
  print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
else:
  dp[0] = stairs[0]
  dp[1] = stairs[0] + stairs[1]
  dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
  
  for i in range(3, N):
    score1 = dp[i-2] + stairs[i]
    score2 = dp[i-3] + stairs[i-1] + stairs[i]
    dp[i] = max(score1, score2)

  print(dp[N-1])