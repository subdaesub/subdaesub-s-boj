def s(n):
    return n*(n+1)//2
n = int(input())
ans = 0
for i in range(1, n-1):
    ans += s(i)
print(ans,3)