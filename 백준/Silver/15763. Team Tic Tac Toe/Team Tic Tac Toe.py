g = []
one = []
two = []

for _ in range(3):
    s = input()
    g.append(s)
l = []
for i in g:
    l.append(i)
for i in range(3):
    l.append(g[0][i] + g[1][i] + g[2][i])
l.append(g[0][0] + g[1][1] + g[2][2])
l.append(g[0][2] + g[1][1] + g[2][0])

for i in l:
    if i.count(i[0]) == 3:
        one.append([i[0]])
    else:
        if i[0] == i[1]:
            two.append([i[0], i[2]])
        elif i[0] == i[2]:
            two.append([i[0], i[1]])
        elif i[1] == i[2]:
            two.append([i[0], i[1]])

two_team = {tuple(sorted(item)) for item in two}
one_team = {tuple(item) for item in one}
print(len(one_team))
print(len(two_team))