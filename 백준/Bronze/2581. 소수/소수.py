a = int(input())
b = int(input())
prime = []
if a <= 2:
    prime.append(2)
    a = 3
clk = False
for i in range(a, b + 1):
    for j in range(2, (i // 2 + 1)):
        if i % j == 0:
            clk = True
            break
    if not clk:
        prime.append(i)
    clk = False
if len(prime) == 0 or b == 1:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))