s = int(input())
i = 0
while True:
    i += 1
    s -= i
    if s < 0:
        break
print(i - 1)