
n = int(input())

#산술평균 : N개의 수들의 합을 N으로 나눈 값
#중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
#최빈값 : N개의 수들 중 가장 많이 나타나는 값
#범위 : N개의 수들 중 최댓값과 최솟값의 차이
from collections import Counter

result = []

for i in range(n) :
  inputNum = int(input())
  result.append(inputNum)

result.sort()

counter = Counter(result).most_common(2)

print(round(sum(result) / len(result)))
print(result[len(result) // 2])
if len(result) > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(counter[0][0])
print(max(result) - min(result))