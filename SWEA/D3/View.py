T = 10

def calc(n,building) :  
    max_top = max(building[n-2],building[n-1],building[n+1],building[n+2])
    re = building[n] - max_top
    if re>0 : return re
    else : return 0

for tc in range(T) :
    N = int(input())
    building = list(map(int,input().split()))
    save = 0
    for i in range(2,N-2) :
        save += calc(i,building)
    print(f"#{tc+1} {save}")