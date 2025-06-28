from itertools import permutations, product

def square(rects):

    for rotated in product(*[[r, (r[1], r[0])] for r in rects]):
        for perm in permutations(rotated):
            a, b, c = perm

            total_area = a[0]*a[1] + b[0]*b[1] + c[0]*c[1]
            side = int(total_area ** 0.5)
            if side * side != total_area:
                return 0

            if a[1] == b[1] == c[1] and a[1] == side and (a[0] + b[0] + c[0]) == side:
                return 1

            if a[0] == b[0] == c[0] and a[0] == side and (a[1] + b[1] + c[1]) == side:
                return 1

            if a[0] == side and a[1] + max(b[1], c[1]) == side:
                if b[1] == c[1] and b[1] == side - a[1] and (b[0] + c[0] == side):
                    return 1

            if a[1] == b[1] and a[1] + c[1] == side:
                if a[0] + b[0] == side and c[0] == side:
                    return 1

    return 0

w = []
for _ in range(3):
    w.append(list(map(int, input().split())))
print(square(w))
