n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

score = 0
for i in range(n):
    score += abs(a[i]) + abs(b[i])

print(score)