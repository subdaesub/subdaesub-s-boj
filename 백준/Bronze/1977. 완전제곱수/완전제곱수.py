import math
a = int(input())
b = int(input())
arr = []
for i in range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b)) + 1):
    arr.append(i * i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])