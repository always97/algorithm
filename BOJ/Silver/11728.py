N, M = map(int,input().split())

arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))

result_arr = []
p1, p2 = 0,0

while p1<N and p2<M :
  if arr_A[p1] <= arr_B[p2] :
    result_arr.append(arr_A[p1])
    p1 += 1
  else :
    result_arr.append(arr_B[p2])
    p2 += 1

result_arr.extend(arr_A[p1:])
result_arr.extend(arr_B[p2:])


print(' '.join(map(str,result_arr)))