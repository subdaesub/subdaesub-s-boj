n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    if b > a and l[i] == 1:
        cnt += (b - a)
print(cnt)