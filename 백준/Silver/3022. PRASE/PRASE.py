t = int(input())
arr = []
warn = 0
for _ in range(t):
    s = input()

    if arr.count(s) > len(arr) // 2:
        warn += 1
    arr.append(s)

print(warn)