n = int(input())
arr = list(map(int, input().split()))

ans = -1
for i in range(51):
    if arr.count(i) == i:
        ans = i

print(ans)