max = 0
people = 0
for _ in range(10):
    a, b = map(int, input().split())
    people += (b - a)
    if people > max:
        max = people
print(max)