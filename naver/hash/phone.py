def solution(phone_book):
    phone = {}
    ans = True 
    
    for p in phone_book :
        phone[p] = 1
    
    for p in phone_book :
        for i in range(1, len(p)):
            if p[0:i] in phone : 
                ans = False
                break
    return ans