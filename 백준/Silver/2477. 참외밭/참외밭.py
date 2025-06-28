k = int(input())
a = []
b = []
n = []
for _ in range(6):
  x, y = map(int, input().split())
  a.append(x)
  b.append(y)
n.append(abs(b[0] * b[1] + b[3] * b[4]))
n.append(abs(b[0] * b[1] - b[3] * b[4]))
n.append(abs(b[1] * b[2] + b[4] * b[5]))
n.append(abs(b[1] * b[2] - b[4] * b[5]))

for i in range(3):
  if n.count(n[i]) == 2:
    print(n[i] * k)
    break