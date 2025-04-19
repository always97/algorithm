def solution(wallet, bill):
    answer = 0
    
    l_wallet = max(wallet[0], wallet[1])
    s_wallet = min(wallet[0], wallet[1])

    l_bill = max(bill[0], bill[1])
    s_bill = min(bill[0], bill[1])
    while l_bill > l_wallet or s_bill > s_wallet :
        answer += 1
        h_bill = l_bill//2
        l_bill = max(s_bill, h_bill)
        s_bill = min(s_bill, h_bill)
    return answer