n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
weight = []
for i in range(len(arr)):
    weight.append(arr[i] * (len(arr) - i))
print(max(weight))