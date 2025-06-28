t = int(input())
for _ in range(t):
    n = int(input())
    print(f'Pairs for {n}:', end = '')
    if n not in [1, 2]:
        a = 1
        b = n - 1
        s = []
        s.append(f'{a} {b}')
        while True:
            a += 1
            b -= 1
            if a < b and a != b:
                s.append(f'{a} {b}')
            else:
                break
        print(f' {s[0]}', end ='')
        if n > 4:
            for i in range(1, len(s)):
                print(f', {s[i]}', end ='')
    print('')