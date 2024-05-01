T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리

for test_case in range(1, T + 1):

  answer = 0

  arr = list(map(int,input().split()))

  arr.sort()

  answer = round((sum(arr[1:9])/8))

  print(f"#{test_case} {answer}")