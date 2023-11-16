n = int(input())

days = [31,28,31,30,31,30,31,31,30,31,30,31];

for i in range(1,n+1) :
  date = input();
  year = (date[:4])
  month = (date[4:6])
  day = (date[6:8])
  answer = '-1'

  if 12 >= int(month) >= 1  :
    if 1 <= int(day) <= days[int(month)-1] :
      answer = f"{year}/{month}/{day}"
  
  
  print(f'#{i} {answer}')