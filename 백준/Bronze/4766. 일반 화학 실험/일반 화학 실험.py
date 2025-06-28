l = []
while True:
    n = float(input())
    if n == 999:
        break
    l.append(n)
for i in range(1, len(l)):
    print(f"{l[i] - l[i - 1]:.2f}")