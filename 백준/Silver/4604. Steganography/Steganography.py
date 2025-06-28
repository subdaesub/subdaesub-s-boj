def code(n):
    if n == 0:
        return ' '
    elif n >= 1 and n <= 26:
        return chr(n + 64)
    elif n == 27:
        return "'"
    elif n == 28:
        return ','
    elif n == 29:
        return '-'
    elif n == 30:
        return '.'
    elif n == 31:
        return '?'

l = ''
clk = False
cnt = 0
ans = []
while True:
    s = input()
    k = ''
    if s == '#':
        break
    elif s == '*':
        for i in range(len(l)):
            if l[i] == ' ' and clk:
                cnt += 1

            elif l[i] == ' ' and not clk:
                cnt += 1
                clk = True

            elif l[i] != ' ' and clk:
                if cnt % 2 == 0:
                    k += '1'
                else:
                    k += '0'
                cnt = 0
                clk = False
        ans.append(k)
        l = ''
    else:
        l += s

for i in ans:
    if len(i) % 5 != 0:
        i += '0' * (5 - (len(i) % 5))
    for j in range(0, len(i), 5):
        print(code(int(i[j:j + 5], 2)), end = '')
    print('')