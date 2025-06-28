arr = []
i = 1
while len(arr) <= 1000:
    for _ in range(i):
        arr.append(i)
    i += 1
a, b = map(int, input().split())
print(sum(arr[a-1:b]))