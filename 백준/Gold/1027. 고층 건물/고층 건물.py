from collections import Counter

n = int(input())
tower = list(map(int, input().split()))
t = []
cnt = 0
clk = True
for i in range(len(tower)):
  for j in range(i + 1, len(tower)):
    for k in range(i + 1, j):
      if tower[j] >= tower[i]:
        if tower[k] >= (k - i) * (tower[j] - tower[i]) / (j - i) + tower[i]:
          clk = False
      else:
        if tower[k] >= tower[i] - (k - i) * (tower[i] - tower[j]) / (j - i):
          clk = False
    if clk:
      cnt += 1
      t.append(i)
      t.append(j)
    clk = True
if n == 1:
  print(0)
else:
  counter = Counter(t)  
  most_common = counter.most_common(1)
  print(most_common[0][1])