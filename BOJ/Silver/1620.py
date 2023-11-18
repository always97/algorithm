import sys
input = sys.stdin.readline

n, m = map(int,input().split())


dogamName = {}
dogamNum = {}

for i in range(1,n+1) :
  value = input().strip()
  dogamName[value] = i
  dogamNum[i] = value

for i in range(m) :
  findValue = input().strip()
  if findValue.isdigit() : 
    # 숫자인경우 이름을출력
    print(dogamNum.get(int(findValue)))
  else  :
    # 문자인 경우 번호 출력
    print(dogamName.get(findValue))


