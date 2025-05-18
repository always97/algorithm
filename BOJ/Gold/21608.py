N = int(input())

student_prefer = {}
student_order = []
classroom = [[0]*N for _ in range(N)]

# 입력
for i in range(N*N):
  student_data = list(map(int,input().split()))
  student_id = student_data[0]
  prefer_list = student_data[1:]
  student_order.append(student_id)
  student_prefer[student_id] = prefer_list


# 자리 배치 
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for student_id in student_order:
  prefer_list = student_prefer[student_id]
  가능한자리 = []
  for i in range(N):
    for j in range(N):
      if classroom[i][j] == 0:
        인접한선호학생수 = 0
        인접한빈자리수 = 0
        for k in range(4):
          nr, nc = i+dr[k], j+dc[k]
          if 0<= nr < N and 0 <= nc < N :
            if classroom[nr][nc] == 0 :
              인접한빈자리수 += 1
            elif classroom[nr][nc] in prefer_list :
              인접한선호학생수 += 1
        가능한자리.append((-인접한선호학생수, -인접한빈자리수,i,j))
  가능한자리.sort()
  최적행, 최적열 = 가능한자리[0][2], 가능한자리[0][3]
  classroom[최적행][최적열] = student_id

score = [0,1,10,100,1000]
result = 0
for i in range(N):
  for j in range(N):
    student_id = classroom[i][j]
    prefer_list = student_prefer[student_id]
    인접선호학생수 = 0
    for k in range(4):
      nr, nc = i+dr[k], j+dc[k]
      if 0<= nr < N and 0<= nc < N :
        if classroom[nr][nc] in prefer_list :
          인접선호학생수 += 1
    result += score[인접선호학생수]

print(result)