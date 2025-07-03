from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
targets = list(map(int, input().split()))
dq = deque(range(1, n + 1))

cnt = 0

for target in targets:
    idx = dq.index(target)
    if idx <= len(dq) // 2:
        dq.rotate(-idx)
        cnt += idx
    else:
        dq.rotate(len(dq) - idx)
        cnt += len(dq) - idx
    dq.popleft()

print(cnt)