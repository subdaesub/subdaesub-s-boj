t = int(input())
for k in range(t):
    n = int(input())
    arr = []
    s = input()
    for i in range(len(s)):
        if s[i] in ['U', 'R', 'Y', 'B']:
            arr.append([s[i]])
        else:
            if s[i] == 'O':
                arr.append(['R', 'Y'])

            elif s[i] == 'P':
                arr.append(['R', 'B'])

            elif s[i] == 'G':
                arr.append(['Y', 'B'])

            elif s[i] == 'A':
                arr.append(['R', 'Y', 'B'])

    cnt = 0
    red, yellow, blue = False, False, False

    print(f'Case #{k + 1}: ', end ='')

    if 'R' in arr[0]:
        red = True
        cnt += 1
    if 'Y' in arr[0]:
        yellow = True
        cnt += 1
    if 'B' in arr[0]:
        blue = True
        cnt += 1

    if n == 1:
        print(cnt)
    else:
        for i in range(1, len(s)):
            if 'R' in arr[i] and not red:
                red = True
                cnt += 1
            elif 'R' not in arr[i] and red:
                red = False

            if 'Y' in arr[i] and not yellow:
                yellow = True
                cnt += 1
            elif 'Y' not in arr[i] and yellow:
                yellow = False

            if 'B' in arr[i] and not blue:
                blue = True
                cnt += 1
            elif 'B' not in arr[i] and blue:
                blue = False
        print(cnt)