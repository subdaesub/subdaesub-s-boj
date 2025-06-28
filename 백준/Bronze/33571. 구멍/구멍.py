s = input()
cnt = 0
for i in s:
    if i in ['A', 'a', 'b', 'D', 'd', 'e', 'g', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', '@']:
        cnt += 1
    elif i == 'B':
        cnt += 2
print(cnt)