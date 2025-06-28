arr = []
max_arr = 0
for _ in range(5):
    s = input()
    arr.append(s)
    if len(s) > max_arr:
        max_arr = len(s)
for i in range(max_arr):
    for j in range(5):
        if len(arr[j]) > i:
            print(arr[j][i], end = '')
