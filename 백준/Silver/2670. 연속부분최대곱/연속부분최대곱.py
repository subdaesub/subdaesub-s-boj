t = int(input())
arr = []
for _ in range(t):
    arr.append(float(input()))
maxnum = 0
tmp = 1
if max(arr) <= 1:
    maxnum = max(arr)
else:
    for i in range(t):
        tmp *= arr[i]
        if tmp > 1:
            if tmp > maxnum:
                maxnum = tmp
        else:
            tmp = 1
print(f'{maxnum:.3f}')