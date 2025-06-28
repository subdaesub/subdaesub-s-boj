n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

index = 1
while True:
    arr_list = []
    for i in range(len(arr)):
        if len(arr[i]) > index:
            arr_list.append(arr[i][:index])
    arr_set = set(arr_list)
    if len(arr_list) == len(arr_set):
        break
    index += 1

print(index)