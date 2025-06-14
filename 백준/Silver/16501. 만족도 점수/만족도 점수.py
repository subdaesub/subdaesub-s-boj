from itertools import permutations

arr = list(map(int, input().split()))

highest = 0

for p in permutations(arr):
    l = list(p)
    highest = max(highest, min((1 - (abs(((l[0] + l[1]) / 2) - ((l[2] + l[3]) / 2)) / 10)), (1 - (abs(((l[4] + l[5]) / 2) - ((l[6] + l[7]) / 2)) / 10))))

print(highest)