import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == '#':
        break

    used = []
    symbols = []
    s_lower = s.lower()

    for i in range(len(s_lower)):
        if s_lower[i] not in used:
            used.append(s_lower[i])
            print(s[i], end = '')
        else:
            if s_lower[i] not in symbols:
                symbols.append(s_lower[i])
            if symbols.index(s_lower[i]) == 0:
                print('*', end = '')
            elif symbols.index(s_lower[i]) == 1:
                print('?', end = '')
            elif symbols.index(s_lower[i]) == 2:
                print('/', end = '')
            elif symbols.index(s_lower[i]) == 3:
                print('+', end = '')
            elif symbols.index(s_lower[i]) == 4:
                print('!', end = '')
    print()