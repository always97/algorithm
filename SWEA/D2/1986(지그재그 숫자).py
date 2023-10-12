T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

answer = [0]*11

for i in range(1,11) :
  if i % 2 == 0 :
    # 짝수면 빼기
    answer[i] = answer[i-1]-i
    #홀수면 더하기
  else :
    answer[i] = answer[i-1]+i


for test_case in range(1, T + 1):
  a = int(input())
  print(f"#{test_case} {answer[a]}")
  