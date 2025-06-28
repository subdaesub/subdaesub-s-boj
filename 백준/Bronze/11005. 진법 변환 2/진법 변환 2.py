arr = []
n, b = map(int, input().split())
while n:
    k = n % b
    arr.append(k)
    n = (n - k) // b
for i in range(-1, -len(arr) - 1, -1):
    if arr[i] < 10:
        print(arr[i], end = '')
    else:
        print(chr(arr[i] + 55), end = '')