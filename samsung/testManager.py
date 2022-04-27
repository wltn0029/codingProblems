import math

n = int(input())
b = 0
c = 0
a = list(map(int, input().split()))
ans = 0

b, c = list(map(int, input().split()))

for i in range(n):
    if a[i]-b <= 0 : ans+=1
    else : ans += 1 + math.ceil((a[i]-b)/c)

print(ans)