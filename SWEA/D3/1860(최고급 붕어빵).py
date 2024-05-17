T = int(input())

for tc in range(1,T+1) :

    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    now_sec = 0
    fish = 0
    possible = True
    for i in range(max(customers)+1):
        if i != 0 and i % M == 0:
            fish += K
        if i in customers:
            if fish == 0:
                possible = False
            else: fish -= 1


    print(f"#{tc} {'Possible' if possible else 'Impossible'}")