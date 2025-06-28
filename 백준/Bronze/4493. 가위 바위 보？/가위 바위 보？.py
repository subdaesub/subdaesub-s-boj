t = int(input())
p1, p2 = 0, 0
for _ in range(t):
    n = int(input())
    for _ in range(n):
        a, b = map(str, input().split())
        if a == b:
            pass
        elif (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        print('Player 1')
    elif p2 > p1:
        print('Player 2')
    else:
        print('TIE')
    p1, p2 = 0, 0