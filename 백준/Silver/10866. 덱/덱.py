from collections import deque
import sys
input = sys.stdin.readline

q = deque()

n = int(input())
for _ in range(n):
    s = input().strip()
    if s.startswith("push_front"):
        _, x = s.split()
        q.appendleft(int(x))
    elif s.startswith("push_back"):
        _, x = s.split()
        q.append(int(x))
    elif s == "pop_front":
        print(q.popleft() if q else -1)
    elif s == "pop_back":
        print(q.pop() if q else -1)
    elif s == "size":
        print(len(q))
    elif s == "empty":
        print(0 if q else 1)
    elif s == "front":
        print(q[0] if q else -1)
    elif s == "back":
        print(q[-1] if q else -1)