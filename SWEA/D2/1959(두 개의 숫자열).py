T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리

for test_case in range(1, T + 1):

  N,M = map(int,(input().split()))

  arrA = list(map(int,(input().split())))
  arrB = list(map(int,(input().split())))

  if N < M : # 더 큰 값이 N, A가 되도록,
    N,M = M,N
    arrA,arrB = arrB,arrA

  abMax = 0

  for i in range(N-M+1) :
    temp = 0
    # 작은 값 크기만큼
    for j in range(M) :
      temp += arrA[j+i] * arrB[j]
    if temp > abMax :
      abMax = temp
  

  print(f"#{test_case} {abMax}")