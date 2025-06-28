n = input()
arr = []
for i in range(len(n)):
    arr.append(int(n[i]))
if 0 in arr and sum(arr) % 3 == 0:
    arr.sort(reverse = True)
    for i in arr:
        print(i, end = '')
else:
    print(-1)
