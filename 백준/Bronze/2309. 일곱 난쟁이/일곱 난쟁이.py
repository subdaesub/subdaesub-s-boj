from itertools import permutations

arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
for i in list(permutations(arr, 7)):
    if sum(i) == 100:
        for k in i:
            print(k)
        break