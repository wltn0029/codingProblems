def do_dp(money) :
    if len(money) <=2 : return max(money)

    dp = [-1] * (len(money))
    dp[-1] = money[-1]
    dp[-2] = max(money[-1], money[-2])
    
    for i in range(len(money)-3, -1, -1):
        dp[i] = max(money[i]+dp[i+2], dp[i+1])
        
    return dp[0]

def solution(money):
    if len(money) == 3 : return max(money)
    return max(money[0]+do_dp(money[2:-1]), do_dp(money[1:]))