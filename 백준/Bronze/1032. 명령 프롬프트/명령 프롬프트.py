n = int(input())
l = []
output = ''
for _ in range(n):
    l.append(input())
for i in range(len(l[0])):
    clk = True
    k = l[0][i]
    for j in l:
        if j[i] != k:
            clk = False
            break
    if clk:
        output += k
    else:
        output += '?'
print(output)