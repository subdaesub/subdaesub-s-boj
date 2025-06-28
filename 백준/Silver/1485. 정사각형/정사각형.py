def l(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

def square(p):
    arr = []
    for i in range(4):
        for j in range(i + 1, 4):
            arr.append(l(p[i], p[j]))
    k = set(arr)
    if len(k) == 2:
        return 1
    return 0

for _ in range(int(input())):
    p = [tuple(map(int, input().split())) for _ in range(4)]
    print(square(p))