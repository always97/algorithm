import heapq
import sys

input = sys.stdin.readline 

N = int(input())

max_heap = []

for _ in range(N) :
  data = int(input())
  if data == 0 :
    if not max_heap :
      print(0)
    else:
      print(-heapq.heappop(max_heap))
  else:
    heapq.heappush(max_heap, -data)
