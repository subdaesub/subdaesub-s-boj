n = int(input())
name = []
for _ in range(n):
    a, b = map(str, input().split())
    name.append([f'{b} {a}'])
name.sort()
for i in range(n):
    a, b = map(str, str(*name[i]).split())
    print(b, a)