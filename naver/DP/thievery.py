def do_dp(money) :
    if len(money) <=2 : return max(money)

    dp = [-1] * (len(money))
    dp[-1] = money[-1]
    dp[-2] = max(money[-1], money[-2])
    
    def getMax(i):
        if dp[i] != -1 : return dp[i]
        else : 
            dp[i]=max(getMax(i+2)+money[i], getMax(i+1))
            return dp[i]

    r = getMax(0)
    return r

def solution(money):
    if len(money) == 3 : return max(money)
    return max(money[0]+do_dp(money[2:-1]), do_dp(money[1:]))