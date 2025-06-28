n, k = map(int, input().split())
arr = []
ans = []
index = 0
for i in range(1, n + 1):
    arr.append(i)
while len(arr) > 0:
    index += (k - 1)
    while index >= len(arr):
        index -= len(arr)
    ans.append(arr[index])
    arr = arr[:index] + arr[index + 1:]
print('<', end = '')
for i in range(n - 1):
    print(f'{ans[i]}, ', end = '')
print(f'{ans[-1]}>')